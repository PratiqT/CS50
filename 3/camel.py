camelcase = input("CamelCase: ")
snakecase = ""
for i in camelcase:
    if i.isupper():
        snakecase += "_" + i.lower()
    else:
        snakecase += i

print("snake_case: " , snakecase)
