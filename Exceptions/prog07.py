def main():

    try:
        a = 1
        b = 0
        c = a / b
    except Exception as err:
        print("Error: {0}".format(err))
    else:
        print("Did not encounter any exception ...")
    finally:
        print("This block is always executed...")

if __name__ == "__main__":
    main()
