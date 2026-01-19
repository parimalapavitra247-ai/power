import sys
def power(base, expo):
    return base ** expo
if __name__ == "__main__":
    try:
        if len(sys.argv) == 3:
            base = int(sys.argv[1])
            expo = int(sys.argv[2])
        else:
            base = int(input("Enter the base number: "))
            expo = int(input("Enter the exponent number: "))

        print("Power:", power(base, expo))

    except ValueError:
        print("Invalid input")
