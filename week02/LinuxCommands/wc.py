import sys

def wc(command = sys.argv[1], filename = sys.argv[2]):
    if command not in ['chars', 'words', 'lines']:
        raise SyntaxError('Wrong command !')

    with open (filename, 'r') as f:
        if command == 'chars':
            print(len(f.read()))

        elif command == 'words':
            x = f.readlines()
            x = [y.split(' ') for y in [i.strip() for i in x]]
            print(sum(len(i) for i in x if i[0] != ''))
            
        elif command == 'lines':
            print(sum(1 for i in f.readlines()))
            

def main():
    wc()

if __name__ == "__main__":
    main()