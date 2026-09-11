due = 50
while due > 0:
    print("Amount Due: ", due)
    value = int(input("Insert Coin: "))
    if value in [5, 10, 25]:
         due -= value
owed = abs(due)
print("Change Owed: ", owed)








