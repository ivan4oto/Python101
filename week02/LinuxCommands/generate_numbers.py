import sys
from random import randint

def generate_numbers(filename = sys.argv[1], numbers = sys.argv[2]):
    
    with open (filename, 'w') as f:
        for i in range(int(numbers)):
            if i != int(numbers)-1:
                f.write(f'{randint(1, 100)} ')
            else:
                f.write(f'{randint(1, 100)}')
def main():
    generate_numbers()

if __name__ == '__main__':
    main()