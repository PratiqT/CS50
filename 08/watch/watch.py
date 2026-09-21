import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.match(r'^<iframe src="https?://(www\.)?youtube\.com/embed/(.+)"></iframe>$', s)
    if not matches:
        return None
    return f"https://youtu.be/{matches.group(2)}"


if __name__ == "__main__":
    main()