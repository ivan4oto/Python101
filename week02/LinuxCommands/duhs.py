import sys
import os

def duhs(path = sys.argv[1]):
    def folder_size(path='.'):
        total = 0
        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += folder_size(entry.path)
        return total

    print(f'{path} size is: {int(folder_size(path))//(1024*1024)} MB')


def main():
    duhs()
    
if __name__ == "__main__":
    main()