import sys

def main():

    if len(sys.argv) != 2:
        print("inválid input")
    try:
        with open(sys.argv[1], 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: file not found")
    except IsADirectoryError:
        print("Error: is a directory")
    except Exception as e:
        print(f"Error: {type(e).__name__}")

if __name__ == '__main__':
    main()