import socket
import threading
import time
from time import sleep

PORT = 8888
HOST = '127.0.0.1'
MAX_CONNECTIONS = 5

# bind socket to address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def start_server():
    server.listen(MAX_CONNECTIONS)
    print(f"Server is listening on port {PORT}.")
    listening = True

    # receive requests
    while listening:
        conn, addr = server.accept()
        # create a thread to handle client request
        thread = threading.Thread(target=handle_client, args=(conn, addr))

        thread.start()


# handle requests
def handle_client(conn, addr):
    print(f"Connected to {addr}")

    # non-blocking socket set to deal with multiple requests
    conn.setblocking(False)

    while True:
        try:
            # receive data from web server
            data = conn.receive(1024)

            print(f"Data: {data.decode('utf-8')}")
        except BlockingIOError:
            print("Trying to receive data...")
            time.sleep(1)
        except Exception as e:
            print(f"Error:{e}")
            print("Closing connection")
            break

def check_connection():
    pass
