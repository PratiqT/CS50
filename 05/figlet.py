import sys
import pyfiglet
font = pyfiglet.FigletFont.getFonts()
if len(sys.argv) == 1:
    text = input("Input: ")
    print(pyfiglet.figlet_format(text))

elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    if sys.argv[2] not in font:
        sys.exit("Invalid usage")
    text = input("Input: ")
    print(pyfiglet.figlet_format(text, font=sys.argv[2]))


else:
    sys.exit("Invalid usage")
