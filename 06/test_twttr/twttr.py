def main():
    word = input("Input: ")
    print("Output:", shorten(word))



def shorten(word):
    new = ""
    for i in word:
        if i not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            new = new + i
    return new




if __name__ == "__main__":
    main()