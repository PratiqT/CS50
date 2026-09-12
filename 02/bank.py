x = input("greetings:")
x = x.strip()
if x.lower().startswith("hello"):
    print("$0")
elif x.lower().startswith("h"):
    print("$20")
else:
    print("$100") 