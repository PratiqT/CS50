def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Plate must be between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Tracking variable to check if numbers have started
    numbers_started = False

    for i in s:
        # Rule 3: No periods, spaces, or punctuation allowed
        if not (i.isalpha() or i.isdigit()):
            return False

        if i.isdigit():
            # Rule 4: The first number used cannot be a '0'
            if not numbers_started and i == '0':
                return False
            numbers_started = True

        elif i.isalpha():
            # Rule 5: No letters can come after a number (Fixes CS50P)
            if numbers_started:
                return False

    # If all checks pass, the plate is valid
    return True




main() 