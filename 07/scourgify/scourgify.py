import sys
import csv
try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")

except IndexError:
    sys.exit("Too few command-line arguments")

try:

    students = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = ({"name":row["name"],"house":row["house"]})
            students.append(student)

    with open(sys.argv[2], "w") as file:
        text = csv.DictWriter(file,fieldnames=["first","last","house"])
        text.writeheader()
        for student in students:
            last, first = student['name'].split(", ")
            text.writerow({"first":first, "last":last, 'house':student["house"]})



except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
