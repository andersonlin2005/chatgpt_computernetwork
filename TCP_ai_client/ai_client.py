import socket

HOST = '192.168.56.1' # 伺服器的 IP 地址
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("請輸入要給 AI 的訊息：")
    s.sendall(message.encode())

    response = s.recv(1024).decode()
    print(f"📥 AI 回應：{response}")
