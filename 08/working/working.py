
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)


    if not matches:
        raise ValueError

    start_hour =int(matches.group(1))
    end_hour = int(matches.group(4))
    start_min = int(matches.group(2) or 0)
    end_min = int(matches.group(5) or 0)
    start_period = matches.group(3)
    end_period = matches.group(6)


    if not (1 <= start_hour <= 12):
        raise ValueError
    if not (1 <= end_hour <= 12):
        raise ValueError
    if not (0 <= start_min <= 59):
        raise ValueError
    if not (0 <= end_min <= 59):
        raise ValueError



    if start_period == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12



    if end_period == "AM":
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12


    return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


if __name__ == "__main__":
    main()