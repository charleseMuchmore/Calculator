def add(num1, num2):
    """Adds"""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies"""
    return num1 * num2

def divide(num1, num2):
    """Divides"""
    return num1 / num2

def print_ops():
    print(" + \n - \n * \n /")

def calculate(first_num, operation, second_num):
    """Calculates two numbers, does addition, subtraction, multiplication, and division, returns a dictionary with the user inputs, and answer"""
    if operation == '+':
        answer = add(first_num, second_num)
    elif operation == '-':
        answer = subtract(first_num, second_num)
    elif operation == '*':
        answer = multiply(first_num, second_num)
    elif operation == '/':
        answer = divide(first_num, second_num)
    else:
        print("An invalid operation has been given")
    return float(answer)

def request_firstnum():
    return float(input("First num: "))
def request_secondnum():
    return float(input("Second num: "))
def request_operation():
    return str(input("Operation: "))

def put_in_dict(given_dictionary, key, value):
    given_dictionary[key] = value