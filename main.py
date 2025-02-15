#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
from datetime import datetime

def generate_ebook(root_dir, output_format="epub", output_name=None):
    """
    生成电子书的主要函数
    :param root_dir: 要扫描的根目录
    :param output_format: 输出格式 (epub/pdf)
    :param output_name: 输出文件名（不包括扩展名）
    """
    # 创建临时工作目录（排除掉以"_"开头的目录）
    temp_dir = os.path.join(root_dir, "_booktemp")
    os.makedirs(temp_dir, exist_ok=True)

    # 生成书籍元数据
    metadata = generate_metadata(root_dir)

    # 创建主 Markdown 文件
    main_md = os.path.join(temp_dir, "main.md")

    with open(main_md, "w", encoding="utf-8") as f:
        # 只写入一次 YAML front matter
        f.write("---\n")
        f.write(f"title: {metadata['title']}\n")
        f.write(f"author: {metadata['author']}\n")
        f.write(f"date: {metadata['date']}\n")
        f.write("lang: zh-CN\n")
        f.write("---\n\n")

        # 递归处理目录结构
        process_directory(root_dir, f, root_dir)

    # 使用 Pandoc 生成电子书

    output_file = os.path.join(root_dir, f"{output_name or metadata['title'] or 'book'}.{output_format}")
    generate_with_pandoc(main_md, output_file, output_format)

    # 如有需要可清理临时文件
    # cleanup_temp_files(temp_dir)

def generate_metadata(root_dir):
    """生成电子书元数据"""
    return {
        "title": os.path.basename(os.path.abspath(root_dir)),
        "author": os.path.basename(os.path.abspath(root_dir)),
        "date": datetime.now().strftime("%Y-%m-%d"),
    }

def process_directory(current_dir, file_handler, root_dir, level=0):
    """递归处理目录结构，同时跳过临时目录和隐藏文件，并按名称顺序排序"""
    # 直接按照字母顺序（忽略大小写）排序所有条目
    for item in sorted(os.listdir(current_dir), key=lambda x: x.lower()):
        # 跳过临时目录和隐藏文件（包括以 "_" 开头的）
        if item.startswith(('_', '.')):
            continue

        path = os.path.join(current_dir, item)
        if os.path.isdir(path):
            header = "#" * (level + 1)
            file_handler.write(f"{header} {item}\n\n")
            process_directory(path, file_handler, root_dir, level + 1)
        else:
            if item.lower().endswith((".html", ".md")):
                file_handler.write(f"## {os.path.splitext(item)[0]}\n\n")
                include_content(path, file_handler)
                file_handler.write("\n\n")

def remove_yaml_front_matter(content):
    """
    检测内容是否以 YAML front matter 开头，如果是则剔除之
    这里要求 YAML 块必须以独占一行的"---"来分隔
    """
    # 去除前导空格和 BOM
    content = content.lstrip()
    if content.startswith("---"):
        lines = content.splitlines()
        # 第1行为"---"，查找下一个仅包含"---"（忽略前后空格）的行
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                # 返回从 YAML 块后面的内容（去掉可能的空行）
                return "\n".join(lines[i+1:]).lstrip()
    return content

def include_content(file_path, file_handler):
    """
    将文件内容插入主文档，处理 Markdown 文件时将剔除其 YAML front matter
    """
    try:
        if file_path.lower().endswith(".html"):
            # 将 HTML 转为 Markdown
            converted = subprocess.check_output(
                ["pandoc", "-f", "html", "-t", "markdown", file_path],
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            file_handler.write(converted)
        elif file_path.lower().endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            # 剔除开头的 YAML front matter（如果存在）
            content = remove_yaml_front_matter(content)
            file_handler.write(content)
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        file_handler.write(f"*[Error processing file: {file_path}]*\n")

def generate_with_pandoc(input_md, output_file, output_format):
    """使用 Pandoc 生成最终电子书"""
    cmd = [
        "pandoc",
        input_md,
        "-o",
        output_file,
        "--toc",
        "--toc-depth=3",
        "--standalone"
    ]

    # 针对 epub 格式的特殊选项，不使用 --epub-metadata，因为元数据已经嵌入到文件中
    if output_format == "epub":
        cmd.extend([
            "-f", "markdown+smart"
        ])
        # 如果存在封面图片（位于 _booktemp/assets/cover.jpg），则添加
        cover_image = os.path.join(os.path.dirname(input_md), "assets", "cover.jpg")
        if os.path.exists(cover_image):
            cmd.extend(["--epub-cover-image=" + cover_image])

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"成功生成电子书: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"生成电子书失败: {e}")
        print(f"错误输出: {e.stderr}")

if __name__ == "__main__":
    base_dir = './'
    for item in os.listdir(base_dir):
        if item.startswith(("_",".")):
            continue
        full_path = os.path.join(base_dir, item)
        if os.path.isdir(full_path):
            print(f"正在处理目录 {full_path}")
            print(f"正在生成电子书 {full_path}")
            generate_ebook(full_path, "epub", output_name=item)
