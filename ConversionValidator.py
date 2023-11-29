import time

def split(input):

    split_input = input.split(',')

    for i, string in enumerate(split_input):
        split_input[i] = string.strip()
        split_input[i] = split_input[i].lower()
    
    if len(split_input) != 2:
        return ["",""]
    
    return split_input

def validateTime(value):
    #Break down value and check to ensure that it is a valid size
    stripped_value = value.strip()
    split_value = stripped_value.split('.')

    if len(split_value) > 2 or split_value == "":
        return False

    # Check to make sure value is a positive number
    for val in split_value:
        if not val.isdigit():
            return False
    
    # Value is valid so return True
    return True

def validateTemp(value):
    #Break down value and check to ensure that it is a valid size
    stripped_value = value.strip()
    positive_value = stripped_value.lstrip('-')
    split_value = positive_value.split('.')

    if len(split_value) > 2 or split_value == "":
        return False

    # Check to make sure value is a number
    for val in split_value:
        if not val.isdigit():
            return False
    
    # Value is valid so return True
    return True

while True:

    time.sleep(0.1)
    valid = False

    with open('user_input.txt', 'r', encoding="utf-8") as f:
        user_input = f.read()
    f.closed

    if user_input != "":
        type, value = split(user_input)

        if type == "time":
            valid = validateTime(value)
        elif type == "temperature":
            valid = validateTemp(value)
        
        with open('validation.txt', 'w', encoding="utf-8") as f:
            f.write(f'{valid}')
        f.closed
