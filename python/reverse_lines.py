#!/usr/bin/env python3
"""倒序输出文件：把文件的每一行按相反顺序打印。

用法:
    python3 reverse_lines.py <文件路径>
"""
import sys


def main():
    if len(sys.argv) != 2:
        print(f"用法: {sys.argv[0]} <文件路径>")
        sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        lines = f.readlines()
    for line in reversed(lines):
        print(line, end="")


if __name__ == "__main__":
    main()
