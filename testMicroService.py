import time

while True:

    user_type = input("Enter type (temperature or time): ")
    user_value = input("Enter value: ")
    with open('user_input.txt', 'w', encoding="utf-8") as f:
        f.write(f'{user_type},{user_value}')
    f.closed

    time.sleep(2)
    with open('validation.txt', 'r', encoding="utf-8") as f:
        input_validity = f.read()
    f.closed
    print(input_validity)

    


    