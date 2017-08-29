def main():

    try:
        a = 1
        b = 0
        if b == 0:
            raise Exception("An exception has been raised...")
        c = a / b
    except Exception as err:
        print("Error: {0}".format(err))
    else:
        print("Did not encounter any exception ...")

if __name__ == "__main__":
    main()
