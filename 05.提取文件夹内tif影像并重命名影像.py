import os
import glob
from pathlib import Path


def extract_tif_files(input_directory, output_directory):
    # 使用 glob 模块查找所有 .tif 文件
    tif_files = glob.glob(os.path.join(input_directory, '**', '*.tif'), recursive=True)

    # 确保输出目录存在
    os.makedirs(output_directory, exist_ok=True)

    # 处理每个 .tif 文件
    for tif_file in tif_files:
        # 获取文件的路径对象
        file_path = Path(tif_file)

        # 获取文件的父文件夹名称
        parent_folder = file_path.parent.name

        # 构建新的文件名：将父文件夹名称添加到原文件名中
        new_file_name = f"{parent_folder}_{file_path.name}"

        # 构建输出文件的完整路径
        output_file_path = os.path.join(output_directory, new_file_name)

        # 打印原始文件路径和输出文件路径
        print(f"Original: {tif_file} -> Output: {output_file_path}")

        # 将文件复制到输出目录（如果需要移动文件，可以将 copy 替换为 rename）
        with open(tif_file, 'rb') as src_file, open(output_file_path, 'wb') as dest_file:
            dest_file.write(src_file.read())

    return tif_files


# 指定输入目录和输出目录
input_directory = 'D:/GIStaian/data_gis/新泰乡镇谷歌影像19级'
output_directory = 'D:/GIStaian/data_gis/新泰乡镇谷歌影像'

# 调用函数提取 .tif 文件并保存到输出目录
tif_files = extract_tif_files(input_directory, output_directory)
