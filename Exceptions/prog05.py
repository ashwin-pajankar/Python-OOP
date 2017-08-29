import sys

def main():

    try:
        a = 1
        b = 1
        c = a / b
#        print("DEBUG: This line will not be executed...")
    except ZeroDivisionError as err:
        print("Error: {0}".format(err))
        print("Running the code for Division by Zero...")
        sys.exit(1)
    except TypeError as err:
        print("Error: {0}".format(err))
        print("Running the code for Type Error...")
        sys.exit(1)
    except Exception as err:
        print("Error: {0}".format(err))
        print("Running the code for general exception...")
        sys.exit(1)
    else:
        print("This block of code did not encounter any exception...")
        sys.exit(0)

#    print("DEBUG: This line will always be executed")


if __name__ == "__main__":
    main()
