import sys
try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
except IndexError:
    sys.exit("Too few command-line arguments")
try:
    with open(sys.argv[1]) as file:
        i = 0
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                continue
            elif not line:
                continue
            else:
                i = i + 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(i)