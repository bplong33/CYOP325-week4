import os
import sys
import signal
from typing import Any

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    clear()
    print('\n\nThanks for using the app!\n\n')
    sys.exit(0)

def get_user_input():
    # this function now requires multiple inputs, and will only support
    # a calculation on 2 values. Adding support for longer expressions
    # (i.e. (4+5) * 3) will require a more complicated implementation
 
    try:
        num1 = int(input("\nEnter the first number:\n> ").strip())
        op = input("Enter an operator (+, -, *, /):\n> ").strip()
        num2 = int(input("Enter the second number:\n> ").strip())
    except ValueError:
        print('\nPlease enter an integer for the two numerical inputs!\n')
        return None

    return {'first': num1, 'operator': op, 'second': num2}


def calculate(vals: dict[str, Any]):
    # the `eval` function now takes in only values supplied by the developer,
    # ensuring we have control over what is executed. 
    #   1. The operator is verified to match one of the few accepted operators
    #   2. The integer inputs are cast to int data types and therefore cannot be code
    #
    # Alternatively, eval could have be removed entirely, as it is not necessary in this case

    try:
        if vals['operator'] in '+-*/':
            result = eval(f"{vals['first']} {vals['operator']} {vals['second']}")
        else:
            print("\nInvalid Operator. Please Try Again...\n")
    except Exception as e:
        print('Invalid Input: ', e)
    return result

def main():
    # handle ctrl + c to quit
    signal.signal(signal.SIGINT, signal_handler)

    clear()

    while True:
        print('-------------------------------')
        print('*          Calculator         *')
        print('-------------------------------')
        print('\nCtrl + C to quit at any time')

        vals = get_user_input()
        if not vals:
            input('Press Enter to continue...')
            clear()
            continue
        result = calculate(vals)
        if result:
            print(f'\nResult: {result}\n')

        input('Press Enter to continue...')
        clear()
