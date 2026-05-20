#!/usr/bin/env python
"""章节字数检查脚本

来源：tomato-novelist check_chapter_wordcount_tomato.py
用途：验证章节正文字数是否在 Genre Profile 规定的范围内。

用法：
  python scripts/check_wordcount.py <章节文件路径>
  python scripts/check_wordcount.py <章节文件路径> --min N --max N
  python scripts/check_wordcount.py --all <目录路径>
"""

import re
import sys
import os
import json
from pathlib import Path

# 将脚本目录加入 sys.path 以便 import shared_utils
sys.path.insert(0, str(Path(__file__).resolve().parent))
from shared_utils import load_genre_profile


def load_wordcount_from_genre_profile():
    """从 Genre Profile 读取字数范围（零依赖）"""
    genre = load_genre_profile()
    wc = genre.get("chapter", {}).get("word_count", {})
    return wc.get("min", 2200), wc.get("max", 2800)


def count_chinese_chars(text):
    """统计中文字符数（不含标点、空格、注释、作者说、追踪卡）"""
    # 移除 Markdown 标题、注释、代码块
    text = re.sub(r'^#.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'[-*_~`]', '', text)

    # 移除分隔线 `---` 之后的所有非正文内容
    # 包括：章末钩子、作者说、隐藏情节追踪卡、writerNotes
    text = re.sub(r'\n---\n.*', '', text, flags=re.DOTALL)

    # 统计中文字符 + 中文标点
    chinese_chars = len(re.findall(r'[一-鿿　-〿＀-￯]', text))
    return chinese_chars


def check_chapter(filepath, min_words=None, max_words=None):
    """检查单个章节的字数"""
    if min_words is None or max_words is None:
        min_words, max_words = load_wordcount_from_genre_profile()
    if not os.path.exists(filepath):
        print(f"[ERROR] 文件不存在: {filepath}")
        return None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    count = count_chinese_chars(content)

    if count < min_words:
        status = "不足"
        icon = "[LOW]"
        suggestion = f"需补充 {min_words - count} 字"
    elif count > max_words:
        status = "超标"
        icon = "[HIGH]"
        suggestion = f"需删减 {count - max_words} 字"
    else:
        status = "合格"
        icon = "[OK]"
        suggestion = "字数在范围内"

    print(f"{icon} {os.path.basename(filepath)}: {count} 字 ({status})")
    if status != "合格":
        print(f"   建议: {suggestion}")
        print(f"   范围: {min_words}-{max_words} 字")

    return {"file": filepath, "count": count, "status": status, "suggestion": suggestion}


def check_all(directory, min_words=None, max_words=None):
    """检查目录下所有章节"""
    if min_words is None or max_words is None:
        min_words, max_words = load_wordcount_from_genre_profile()
    results = []
    for f in sorted(os.listdir(directory)):
        if f.endswith('.md') and not f.endswith('_memo.md') and not f.endswith('_context.json'):
            filepath = os.path.join(directory, f)
            result = check_chapter(filepath, min_words, max_words)
            if result:
                results.append(result)

    # 汇总
    total = len(results)
    ok = sum(1 for r in results if r['status'] == '合格')
    low = sum(1 for r in results if r['status'] == '不足')
    high = sum(1 for r in results if r['status'] == '超标')

    print(f"\n--- 汇总 ---")
    print(f"总章节数: {total}")
    print(f"[OK] 合格: {ok}")
    print(f"[LOW] 不足: {low}")
    print(f"[HIGH] 超标: {high}")
    print(f"合格率: {ok/total*100:.1f}%" if total > 0 else "N/A")

    return results


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法:")
        print("  python scripts/check_wordcount.py <章节文件路径> [--min N] [--max N]")
        print("  python scripts/check_wordcount.py --all <目录路径> [--min N] [--max N]")
        sys.exit(1)

    min_words, max_words = load_wordcount_from_genre_profile()

    # 解析参数
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--min' and i + 1 < len(args):
            min_words = int(args[i + 1])
            i += 2
        elif args[i] == '--max' and i + 1 < len(args):
            max_words = int(args[i + 1])
            i += 2
        elif args[i] == '--all' and i + 1 < len(args):
            check_all(args[i + 1], min_words, max_words)
            sys.exit(0)
        else:
            filepath = args[i]
            check_chapter(filepath, min_words, max_words)
            i += 1
    print(f"[INFO] word count range: {min_words}-{max_words} (source: Genre Profile)")
