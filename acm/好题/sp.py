#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
from collections import defaultdict
from pathlib import Path

FILE = '怯战蜥蜴2.md'          # 待拆分的长文档
ENC  = 'utf-8'

# 彩色提示，Windows 也支持
def warn(msg):
    print(f'\033[33m⚠️  {msg}\033[0m')

def main():
    if not os.path.isfile(FILE):
        exit(f'❌  当前目录找不到 {FILE}')

    written = 0
    text = Path(FILE).read_text(encoding=ENC)
    # 1. 先按一级标题切成大块，split 会丢掉 # 本身，手动补上
    parts = re.split(r'^#\s+', text, flags=re.M)
    for part in parts[1:]:          # 第 0 段是 # 之前的东西，丢弃
        # 取出第一行当文件夹名
        folder, _, body = part.partition('\n')
        folder = folder.strip()
        Path(folder).mkdir(exist_ok=True)

        # 2. 在本块里再切所有二级标题
        for m in re.finditer(r'##\s+(.+?)\s*\n(.*?)(?=^##\s|^#\s|\Z)', body, re.M | re.S):
            file_title = m.group(1).strip()
            body_text  = m.group(2)
            safe_name  = re.sub(r'[\\/:*?"<>|]', '_', file_title)

            # 3. 重名检测
            base_path = Path(folder) / f'{safe_name}.md'
            path = base_path
            counter = 1
            while path.exists():
                path = base_path.with_name(f'{safe_name}({counter}).md')
                counter += 1
            if counter > 1:
                warn(f'{folder}/{safe_name}.md 已存在，自动重命名为 {path.name}')

            # 4. 写文件
            path.write_text(f'## {file_title}\n{body_text}', encoding=ENC)
            written += 1

    print(f'✅  拆分完成，共生成 {written} 个文件')
if __name__ == '__main__':
    main()