import sys

def sum_numbers(numbers = sys.argv[1]):
    with open (numbers, 'r') as f:
        x = sum(int(i) for i in f.read().split(' '))
        print(x)
        
def main():
    sum_numbers()

if __name__ == "__main__":
    main()