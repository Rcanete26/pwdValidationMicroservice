def password_validate(recieved_dict): 
    result = lower_len(recieved_dict)
    result = upper_len(recieved_dict)
    result = digit(recieved_dict)
    result = upper_case(recieved_dict)
    result = lower_case(recieved_dict)
    result = symbol(recieved_dict)
    return result


def lower_len(recieved_dict):
    result = True
    if len(recieved_dict['password']) < recieved_dict['lower_length']:
        result = False
    return result


def upper_len(recieved_dict):
    result = True
    if len(recieved_dict['password']) > recieved_dict['upper_length']:
        result = False
    return result


def digit(recieved_dict):
    result = True
    if not (any(character.isdigit() for character in recieved_dict['password']) 
            and recieved_dict['digit'] != False):
        result = False
    return result


def upper_case(recieved_dict):
    result = True
    if not (any(character.isupper() for character in recieved_dict['password']) 
            and recieved_dict['uppercase'] != False):
        result = False
    return result


def lower_case(recieved_dict):
    result = True
    if not (any(character.islower() for character in recieved_dict['password']) 
            and recieved_dict['lowercase'] != False):
        result = False
    return result


def symbol(recieved_dict):
    symbols = ['!', '@', '-', '_', '&', '#', '%']
    result = True
    if not (any(character in symbols for character in recieved_dict['password']) 
            and recieved_dict['symbol'] != False):
        result = False
    return result