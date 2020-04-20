import sys

def cat2(arguments = sys.argv[1:]):
    for a in arguments:
        with open (a, 'r') as f:
            print('\n')
            result  = f.read()
            print(result)
        
def main():
    cat2()

if __name__ == "__main__":
    main()