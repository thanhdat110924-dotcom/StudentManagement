def enter_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Must be a number!")


def enter_score(message):
    while True:
        try:
            score = float(input(message))
            if not (0 <= score <= 100):
                print("Score must be between 0 and 100!")
                continue 
            return score
        except ValueError:
            print("Must be a number!")