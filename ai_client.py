import socket

# 用戶端主函數
def start_client(host='172.20.10.8', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        while True:
            # 讀取用戶輸入
            question = input("Enter your question (or 'quit' to exit): ")
            if question.lower() == 'quit':
                break
            
            # 發送問題到伺服器
            client_socket.send(question.encode('utf-8'))
            
            # 接收伺服器回答
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server response: {response}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()
