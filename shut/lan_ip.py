import socket

def get_local_ip():
    try:
        # 使用socket模块获取本地IP地址
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # 连接到Google的公共DNS服务器
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print("获取局域网 IP 地址失败:", e)
        return None

if __name__ == '__main__':
    # 获取局域网 IP 地址
    local_ip = get_local_ip()
    print("局域网 IP 地址:", local_ip)