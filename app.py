import socket

print(""" 

            _  __               _____                  ____ _ _            _   
            | |/ /_ __ _   _ _ _|_   _|__  _ __        / ___| (_) ___ _ __ | |_ 
            | ' /| '__| | | | '_ \| |/ _ \| '_ \ _____| |   | | |/ _ \ '_ \| __|
            | . \| |  | |_| | |_) | | (_) | | | |_____| |___| | |  __/ | | | |_ 
            |_|\_\_|   \__, | .__/|_|\___/|_| |_|      \____|_|_|\___|_| |_|\__|
                    |___/|_|                                                 

            [*] Created By KrypTon                    [*] KrypTon Client for victeme

""")

def start_client(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 12345))

    try:
        while True:
            message = input("Enter message to send to the server (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())
            response = client_socket.recv(1024)
            print(f"Received from server: {response.decode()}")
    except KeyboardInterrupt:
        pass
    finally:
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    server_ip = input("Enter the server IP address: ")
    start_client(server_ip)
