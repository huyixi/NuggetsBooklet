
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO
import re
from tqdm import tqdm

def download_image(url, output_dir):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        image_name = os.path.basename(url)
        image_path = os.path.join(output_dir, image_name)
        img.save(image_path)
        print(f"已下载并保存图像：{image_path}")
        return image_path
    except Exception as e:
        print(f"图像下载失败:{url},error:{e}")
        return None

def compress_image(image_path, output_dir=None, max_size=(200, 200)):
    """压缩图像并保存"""
    try:
        with Image.open(image_path) as img:
            img.thumbnail(max_size,Image.Resampling.LANCZOS)

            if output_dir:
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                compressed_path = os.path.join(output_dir, os.path.basename(image_path))
            else:
                compressed_path = image_path

            img.save(compressed_path, quality=50)
            print(f"压缩图像: {compressed_path}")
            return compressed_path
    except Exception as e:
        print(f"压缩图像失败: {image_path}, 错误: {e}")
        return None

def process_image_urls_in_md(md_file, output_dir):
    """处理 Markdown 文件中的所有图像链接：下载并压缩"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    image_urls = re.findall(r'!\[.*?\]\((http[^\)]+)\)', content)

    compressed_images = []
    for url in image_urls:
        image_path = download_image(url, output_dir)
        if image_path:
            compressed_image_path = compress_image(image_path, output_dir)
            if compressed_image_path:
                compressed_images.append(compressed_image_path)
                content = content.replace(url, os.path.basename(compressed_image_path))

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return compressed_images

def generate_ebook(root_dir, output_format="epub", output_name=None):
    """生成电子书的主要函数"""
    temp_dir = os.path.join(root_dir, "_booktemp")
    os.makedirs(temp_dir, exist_ok=True)

    # 为图片创建专门的目录
    images_dir = os.path.join(temp_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    metadata = generate_metadata(root_dir)
    main_md = os.path.join(temp_dir, "main.md")

    with open(main_md, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: {metadata['title']}\n")
        f.write(f"author: {metadata['author']}\n")
        f.write(f"date: {metadata['date']}\n")
        f.write("lang: zh-CN\n")
        f.write("---\n\n")

        process_directory(root_dir, f, root_dir, images_dir)

    # 处理Markdown中的在线图片
    process_image_urls_in_md(main_md, images_dir)

    output_file = os.path.join(root_dir, f"{output_name or metadata['title'] or 'book'}.{output_format}")
    generate_with_pandoc(main_md, output_file, output_format)

def generate_metadata(root_dir):
    """生成电子书元数据"""
    return {
        "title": os.path.basename(os.path.abspath(root_dir)),
        "author": os.path.basename(os.path.abspath(root_dir)),
        "date": datetime.now().strftime("%Y-%m-%d"),
    }

def process_directory(current_dir, file_handler, root_dir, level=0):
    """递归处理目录结构，同时跳过临时目录和隐藏文件，并按名称顺序排序"""
    for item in sorted(os.listdir(current_dir), key=lambda x: x.lower()):
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
    """检测内容是否以 YAML front matter 开头"""
    content = content.lstrip()
    if content.startswith("---"):
        lines = content.splitlines()
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[i+1:]).lstrip()
    return content

def include_content(file_path, file_handler):
    """将文件内容插入主文档，处理 Markdown 文件时剔除 YAML front matter"""
    try:
        if file_path.lower().endswith(".html"):
            converted = subprocess.check_output(
                ["pandoc", "-f", "html", "-t", "markdown", file_path],
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            file_handler.write(converted)
        elif file_path.lower().endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
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

    if output_format == "epub":
        cmd.extend([
            "-f", "markdown+smart"
        ])
        cover_image = os.path.join(os.path.dirname(input_md), "assets", "cover.jpg")
        if os.path.exists(cover_image):
            cmd.extend(["--epub-cover-image=" + cover_image])

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"成功生成电子书: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"生成电子书失败: {e}")
        print(f"错误输出: {e.stderr}")

if __name__ == "__main__":
    base_dir = './'
    dirs_to_process = [
        item for item in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, item))
        and not item.startswith(("_", "."))
    ]

    successful = 0
    failed = 0

    with tqdm(dirs_to_process, desc="处理目录") as pbar:
        for item in pbar:
            full_path = os.path.join(base_dir, item)
            pbar.set_description(f"正在处理: {item}")

            try:
                if generate_ebook(full_path, "epub", output_name=item):
                    successful += 1
                    print(f"✓ 成功处理: {item}")
                else:
                    failed += 1
                    print(f"✗ 处理失败: {item}")
            except Exception as e:
                failed += 1
                print(f"✗ 处理出错 {item}: {str(e)}")
                continue

    print(f"\n处理完成! 成功: {successful}, 失败: {failed}")
