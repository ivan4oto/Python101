import sys

def reduce_file_path(path = sys.argv[1]):
    pathsplit = path.split('/')
    resultpath = []
    print(pathsplit)
    for i in pathsplit:
        resultpath.append(i)
        if i == '..':
            resultpath = resultpath[:-2]
    toIgnore = ['', '..', '.']
    resultpath = '/'.join([x for x in resultpath if x not in toIgnore]) + '/'

    print(resultpath)

def main():
    reduce_file_path()

if __name__ == "__main__":
    main()