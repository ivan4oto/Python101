import zipfile
from os import listdir
from os.path import isfile, join

def book_reader(bookpath):
    #extracting the book in subderictory
    with zipfile.ZipFile(bookpath, 'r') as zip_ref:
        zip_ref.extractall('./book')
    #list of bookfiles
    bookfiles = [f for f in listdir('./book/') if isfile(join('./book/', f))]
    for file in bookfiles:
        #making a generator for each line
        lines = (line for line in open(f"./book/{file}"))
        #prompts for input
        z = True
        #deals with first "title"
        toprint = f'Star of file: {file} \n \n ' + next(lines) + '\n'
        print('To start reading, press "Space".')
        while z:
            if input('') == ' ':
                t = True
                while t:
                    try:
                        x = next(lines)
                        if x.startswith('#'):
                            print(toprint)
                            toprint = x
                            t = False
                            break
                        else:
                            toprint+=x
                    except Exception:
                        print(toprint)
                        print('This was the end of the file\n')
                        if file != bookfiles[-1]:
                            print('If you wish to continue reading. Press "Space". If not, press something else.')
                        elif file == bookfiles[-1]:
                            print('This is the end of the book.')
                        z = False
                        break
            else:
                break
