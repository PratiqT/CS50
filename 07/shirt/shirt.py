import sys
import os
from PIL import Image, ImageOps

try:

    if len(sys.argv) >3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) <3:
        sys.exit("Too few command-line arguments")


    input_extensions = os.path.splitext(sys.argv[1])[1].lower()
    output_extensions = os.path.splitext(sys.argv[2])[1].lower()
    allowed_extensions = [".jpeg",".jpg",".png"]


    if input_extensions not in allowed_extensions:
        sys.exit("Invalid input")
    elif output_extensions not in allowed_extensions:
            sys.exit("Invalid output")
    elif input_extensions != output_extensions:
         sys.exit("Input and output have different extensions")

except IndexError:
    sys.exit("Too few command-line arguments")

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt_image = Image.open("shirt.png")

resized_image = ImageOps.fit(input_image, shirt_image.size)

resized_image.paste(shirt_image, shirt_image)

resized_image.save(sys.argv[2])