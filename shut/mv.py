import shutil

# 源文件路径
source_path = '/path/to/source/file.txt'

# 目标文件路径（确保目标路径的目录存在，否则会抛出FileNotFoundError）
destination_path = '/path/to/destination/file.txt'

if '__name__' == '__main__':
    # 使用shutil.copy()复制文件
    shutil.copy(source_path, destination_path)
