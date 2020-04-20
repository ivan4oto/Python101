import sys

def cat(arguments = sys.argv[1]):
    with open (arguments, 'r') as f:
        result  = f.read()
        print(result)
        
def main():
    cat()

if __name__ == "__main__":
    main()