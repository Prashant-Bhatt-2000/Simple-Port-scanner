import socket

ip = socket.gethostbyname(socket.gethostname())
print(f"Starting Scan on {ip}")

for port in range(65535):

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind((ip, port))

    except:
        print("[open port]: ", port)

server.close()
