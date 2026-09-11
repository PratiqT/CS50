months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    date = input("Date: ")

    try:
        if "/" in date:
            month, day, year = date.split("/")
        else:
            if "," not in date:
                continue

            month_name, day, year = date.split(" ")
            day = day.replace(",", "")
            month = months.index(month_name) + 1

        month = int(month)
        day = int(day)

        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break

    except ValueError:
        pass