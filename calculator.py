print('Simple calculator app')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

def modulus (x, y):
    return x % y

def power (x, y):
    return x ** y

def square_root (x):
    return x ** 0.5


finished = False


def check_if_finished ():
    """ Checks whether the user wants to finish or not"""
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish? (y/n)')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print("Response must be either 'y' or 'n', try again")
    return ok_to_finish

def get_operation_choice ():
    input_ok = False
    while not input_ok:
        print('Menu options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('\t5. Remainder')
        print('\t6. Power')
        print('-------------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4', '5', '6'):
            input_ok = True
        else:
            print('Invalid input (must be 1-6)')
    print('------------------')
    return user_selection

def get_num_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be a number')
        value_as_string = input(message)
    return float(value_as_string)

def get_numbers_from_user ():
    num_1 = get_num_input('Input the first number:')
    num_2 = get_num_input('Input the second number:')
    return num_1, num_2

while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)
    elif menu_choice == '5':
        result = modulus(n1, n2)
    elif menu_choice == '6':
        result = power(n1, n2)
    print('Result:', result)
    print('==================')
    finished = check_if_finished()
