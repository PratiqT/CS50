import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")     
                continue

            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")

        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass




def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()