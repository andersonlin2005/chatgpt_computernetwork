import socket

HOST = '0.0.0.0'
PORT = 12345

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"AI TCP Server is running on port {PORT}...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            with conn:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(f"Received from client: {data}")

                # AI 回應邏輯（這裡你可以換成真正的 AI 模型）
                response = f"AI 回應：你說的是「{data}」"
                conn.sendall(response.encode())

if __name__ == '__main__':
    run_server()
