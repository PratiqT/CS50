while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
        elif y == 0:
            continue
        elif x < 0 or y < 0:
            continue
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
z = round(x/y*100)
if z >= 99:
    print("F")
elif z <= 1:
    print("E")
else:
        print(f"{z}%")
