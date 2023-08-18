import socket
import pickle
from pwd_validate import password_validate

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 4211))
server.listen(8)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.bind((socket.gethostname(), 4211))
    stream.listen()
    while True:
        conn, addr = stream.accept()
        with conn:
            while True:
                recieved_dict = pickle.loads(conn.recv(4211))
                print(recieved_dict)
                if not recieved_dict:
                    print("Client disconnect")
                    break
                if len(recieved_dict) > 1:
                    result = password_validate(recieved_dict)
                    conn.send(bytes(str(result), "utf-8"))

