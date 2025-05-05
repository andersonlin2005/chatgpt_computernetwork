import socket
import threading
import google.generativeai as genai
import os

# 初始化 Google Gemini API
api_key = os.getenv("GOOGLE_API_KEY")  # 建議從環境變數讀取
if not api_key:
    api_key = "AIzaSyCqZmKX82_ILtUcKrlnqu2D3CoTwk_aSpk"  # 替換為你的 API Key（僅用於測試，建議使用環境變數）
genai.configure(api_key=api_key)

# 生成回答的函數
def generate_response(question):
    try:
        response = genai.GenerativeModel("gemini-2.0-flash").generate_content(question)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# 處理單個用戶端的函數
def handle_client(client_socket, addr):
    print(f"New connection from {addr}")
    try:
        while True:
            # 接收用戶端發送的問題
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received from {addr}: {data}")
            
            # 使用 Gemini API 生成回答
            response = generate_response(data)
            print(f"Response to {addr}: {response}")
            
            # 將回答發送回用戶端
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        client_socket.close()
        print(f"Connection closed from {addr}")

# 主伺服器函數
def start_server(host='172.20.10.8', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            client_socket, addr = server_socket.accept()
            # 為每個用戶端啟動一個新執行緒
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()