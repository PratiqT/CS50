word = input("input: ")
result = ""
for i in word:
    if i not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        result += i


print("Output:", result) 



