import random
while True:
    try:
        x = int(input("Level: "))
        if x>0:
            break
    except ValueError:
        continue
n = random.randint(1,x)
while True:
    try:
        y = int(input("Guess: "))
        if y<= 0:
            continue
    except ValueError:
        continue
    if y > n:
        print("Too large!")


    elif y < n:
        print("Too small!")


    elif y == n:
        print("Just right!")
        break

