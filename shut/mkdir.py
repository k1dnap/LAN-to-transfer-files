import os

def create_folders():
    try:
        # 获取当前程序路径
        current_path = os.path.abspath(__file__)

        # 获取上三级目录
        parent_path = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))

        # 在上三级目录下创建一个新的文件夹
        new_folder_path = os.path.join(parent_path, "Dir")
        os.makedirs(new_folder_path, exist_ok=True)

        # 返回新创建文件夹的绝对路径
        return new_folder_path

    except Exception as e:
        print("创建文件夹时发生错误:", e)
        return None


# 调用函数并打印新文件夹的绝对路径
# new_folder_absolute_path = create_folders()
# if new_folder_absolute_path:
#     print("新文件夹的绝对路径:", new_folder_absolute_path)
# else:
#     print("文件夹创建失败")