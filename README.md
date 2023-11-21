# CS361 - Conversion Validation Microservice

## Steps to run project:

- git clone repo
- navigate to root project folder
- run ConversionValidator.py by entering:
```
python3 ConversionValidator.py
```

## To request that the microservice validates an input:
- run ConversionValidator.py by entering:
```
python3 ConversionValidator.py
```
- write the data to validate to the user_input.txt file in the following format
```
<type,value>
```

## To recieve data from the microservice:
- After writing to the user_input.txt file, read the text from the validation.txt file. To ensure that the microservice has time to process the input and provide a response, I recommend having the calling program wait for >0.5 sec prior to reading from validation.txt.

## Example of writing and receiving from the necessary files:

```
with open('user_input.txt', 'w', encoding="utf-8") as f:
    f.write(f'{user_type},{user_value}')
f.closed

time.sleep(2)

with open('validation.txt', 'r', encoding="utf-8") as f:
    input_validity = f.read()
f.closed
```

## UML sequence diagram showing communication between main program and the microservice

