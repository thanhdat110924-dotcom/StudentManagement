def enter_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Must be a number!")
