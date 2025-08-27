import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("inválido input")
        return
    try:
        num = float(sys.argv[1])
        print(num)
    except ValueError:
        print("invalid value")

if __name__ == '__main__':
    main()