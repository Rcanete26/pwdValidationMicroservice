import socket
import pickle
from pwd_validate import password_validate

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 4211))
server.listen(8)

while True:
    clientsocket, address = server.accept()
    print(f"I think you have a connection from {address}")
    clientsocket.send(bytes("You are connected to the server", "utf-8"))
    recieved_dict = pickle.loads(clientsocket.recv(4211))
    print(recieved_dict)
    if len(recieved_dict) < 1:
        break
    else:
        result = password_validate(recieved_dict)
        clientsocket.send(bytes(str(result), "utf-8"))

"""What to recieve a dictionary like so
{
password: password being validated
upper_length: (int) upper bound of password
lower_length: (int) lower bound of password
digit: (int) should be 0(digit not needed) or 1(digit needed)
uppercase: (int) should be 0(uppercase not needed) or 1(uppercase  needed)
lowercase: (int) should be 0(lowercase not needed) or 1(lowercase needed)
symbol: (int) should be 0(symbol not needed) or 1(symbol needed), will also have an array of the symbols that are allowed.
}
"""
