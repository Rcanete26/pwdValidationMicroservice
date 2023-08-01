def password_validate(recieved_dict): 
    symbols = ['!', '@', '-', '_', '&', '#', '%']
    result = True

    if len(recieved_dict['password']) < recieved_dict['lower_length']:
        result = False
    
    if len(recieved_dict['password']) > recieved_dict['upper_length']:
        result = False

    if not any(character.isdigit() for character in recieved_dict['password']) and recieved_dict['digit'] != False:
        result = False

    if not any(character.isupper() for character in recieved_dict['password']) and recieved_dict['uppercase'] != False:
        result = False

    if not any(character.islower() for character in recieved_dict['password']) and recieved_dict['lowercase'] != False:
        result = False

    if not any(character in symbols for character in recieved_dict['password']) and recieved_dict['symbol'] != False:
        result = False
    return result