class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass

def main():

    number = 10

    try:

        i_num = int(input("Please enter an interger: "))

        if i_num < number:
            raise ValueTooSmallError
        if i_num > number:
            raise ValueTooLargeError
        else:
            print("Perfect!")
    except ValueTooSmallError:
        print("The value is too small!")
    except ValueTooLargeError:
        print("The value is too large!")
    except Exception:
        print("Unexpected error!")
            

if __name__ == "__main__":
    main()
