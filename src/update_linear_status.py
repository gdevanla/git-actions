import sys

def main():
    print(sys.argv)
    print('called main')

print(f'inside module {__name__=}')
if __name__ == '__main__':
    main()
