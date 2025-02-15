import os
import shutil

def copy_epub_files(src_dir, dest_dir):
    """查找并复制所有 .epub 文件到目标文件夹"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源目录及其子目录
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(".epub"):
                # 获取源文件路径
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                # 如果目标文件夹中没有该文件，才复制
                if not os.path.exists(dest_file):
                    shutil.copy2(src_file, dest_file)  # 保留文件元数据
                    print(f"复制文件: {src_file} 到 {dest_file}")
                else:
                    print(f"跳过文件（已存在）: {dest_file}")

if __name__ == "__main__":
    src_directory = "./"  # 修改为源文件夹路径
    dest_directory = "./epub/"  # 修改为目标文件夹路径

    copy_epub_files(src_directory, dest_directory)
    print("\n所有 epub 文件复制完成！")
