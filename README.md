# pwdValidationMicroservice
Microservice for password validation

Requesting Data:
To request data the microservice will wait for a connection. When a Connection is made to the Microservice it will send a message to the client to show that a connection was made.
After a connection is made the user should send the data in the form of a dictionary with specified key value pairs. When sending the dictionary it should be pickled so that it 
can be sent through the socket with no issue ( the microservice will decode it upon recieving).
![example call]([Paste_link_here](https://github.com/Rcanete26/pwdValidationMicroservice/blob/main/Screenshot%20(15).png))
example_dictionary:{
'password': password being validated
'upper_length': (int) upper bound of password
'lower_length': (int) lower bound of password
'digit': (bool) should be False(digit not needed) or True(digit needed)
'uppercase': (bool) should be False(uppercase not needed) or True(uppercase  needed)
'lowercase': (bool) should be False(lowercase not needed) or True(lowercase needed)
'symbol': (bool) should be False(symbol not needed) or True(symbol needed), will also have an array of the symbols that are allowed.
}
Example Send:
data = pickle.dumps(example_dictionary)
client.send(all)

Revieving Data:
When recieving data from the microservice, after a connection the client should recieve a message to ensure that a connection was established. After the connection is verified and the 
data is sent the microservice will send back a True or False which represents the outcome of the validation. If the sent message is True the password contains all the characteristics 
that was asked to be verified. If the sent message is False the password is missing/does not meet one of the requirments asked for validation. As a note if the microservice is sent a
empty dictionary it will close and stop functioning to prevent sending false information.
