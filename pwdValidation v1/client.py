import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 4211))


example_send = {
    'password': 'Password1234ABCSTRE!',
    'upper_length': 20,
    'lower_length': 0,
    'digit': True,
    'uppercase': True, 
    'lowercase': True, 
    'symbol': True
    }

message = client.recv(1024)  # recieve the connetion message
print(message.decode("utf-8"))  
file = pickle.dumps({})  # encode dictionary + characteristics to validate
client.sendall(file)     
validation_result = client.recv(1024)    # reviece result of validation
print(validation_result.decode("utf-8"))  
