import socket

print("""   
             _  __               _____                ____                           
            | |/ /_ __ _   _ _ _|_   _|__  _ __      / ___|  ___ _ ____   _____ _ __ 
            | ' /| '__| | | | '_ \| |/ _ \| '_ \ ____\___ \ / _ \ '__\ \ / / _ \ '__|
            | . \| |  | |_| | |_) | | (_) | | | |_____|__) |  __/ |   \ V /  __/ |   
            |_|\_\_|   \__, | .__/|_|\___/|_| |_|    |____/ \___|_|    \_/ \___|_|   
                       |___/|_|        
      
            [*] Created By : KrypTon        [*] Serve For Victeme
      
        """)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces on port 12345
    server_socket.listen(5)
    print("Server started, waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                response = f"Server received: {data.decode()}"
                client_socket.send(response.encode())
            except ConnectionResetError:
                break
        
        client_socket.close()
        print(f"Connection with {client_address} closed")

if __name__ == "__main__":
    start_server()
