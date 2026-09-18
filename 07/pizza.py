import sys
import csv
from tabulate import tabulate
try:

    if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

except IndexError:
    sys.exit("Too few command-line arguments")

try:

    with open(sys.argv[1]) as file:
        lines = csv.reader(file)
        print(tabulate(lines, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
     sys.exit("File does not exist")