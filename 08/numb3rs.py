import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if not matches:
        return False
    numbers = matches.groups()

    for number in numbers:
        if len(number) > 1 and number.startswith("0"):
            return False
        number = int(number)
        if number < 0 or number > 255:
            return False


    return True




if __name__ == "__main__":
    main()