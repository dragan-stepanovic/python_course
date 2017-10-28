import sys


def main(filename):
    file = open(filename, mode='rt', encoding='utf-8')
    for line in file:
        print(line)

    file.close()


if __name__ == '__main__':
    main(sys.argv[1])

# this is run from cmd line with -> py files.py airtravel.py
