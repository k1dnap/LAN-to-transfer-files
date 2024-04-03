import os
import http.server
import socketserver
from shut.mkdir import create_folders
from shut.lan_ip import get_local_ip


def start_simple_http_server(host, port, directory):
    """
    启动HTTP服务器。

    参数:
    - host: 服务器监听的IP地址，可自行更改，如改为'0.0.0.0'（监听所有网络接口）
    - port: 服务器监听的端口号，默认为8000
    - directory: 服务器目录，默认为主程序的上级目录'.'
    HOST目前修改为当前局域网IP
    """
    # 切换到指定目录
    os.chdir(directory)

    # 创建服务器
    handler = http.server.SimpleHTTPRequestHandler
    server = socketserver.TCPServer((host, port), handler)

    # 打印服务器启动信息
    print(f"服务器正在监听 {host}:{port}，在浏览器中访问：http://{host}:{port}/")

    try:
        # 启动服务器
        server.serve_forever()
    except KeyboardInterrupt:
        # 捕获Ctrl+C信号并关闭服务器
        print("\n服务器已关闭。")
        server.server_close()

    # 启动服务器
    server.serve_forever()

# 使用函数启动HTTP服务器
if __name__ == "__main__":
    HOST = get_local_ip()  # 服务器IP地址
    DIRECTORY = create_folders()  # 服务器目录
    PORT = 8000  # 服务器端口
    start_simple_http_server(host=HOST, port=PORT, directory=DIRECTORY)