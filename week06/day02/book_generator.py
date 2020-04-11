from random import shuffle

def book_generator(chapters_count, chapters_length, bookname = 'newly_generated_book'):
    with open('randomtext.txt') as f:
        lines = f.read()
    lines = lines.split(' ')
    x = 0
    newlines = []
    for i in range(chapters_length):
        if x > len(lines)-1:
            x = 0
        newlines.append(lines[x])
        x += 1
    book = open(f'{bookname}.txt', 'w')
    for y in range(chapters_count):
        shuffle(newlines)
        book.write(f"# Chapter {y}\n \n" + " ".join(newlines).capitalize() + '\n\n')
    book.close()
    


def main():
    pass

if __name__ == "__main__":
    main()