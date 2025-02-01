import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    return input("\nEnter a math expression ('q' to quit):\t")

def calculate(exp):
    return eval(exp)

def main():

    clear()

    while True:
        print('-------------------------------')
        print('*          Calculator         *')
        print('-------------------------------')

        expression = get_user_input()
        if expression == 'q':
            break

        print(f'\nResult: {calculate(expression)}\n')

        input('Press Enter to continue...')
        clear()


