from os.path import splitext
from PIL import Image, ImageOps
import sys


if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
    sys.exit('Input and output have different extensions')

elif splitext(sys.argv[1])[1].lower() not in ['.jpg', '.jpeg', '.png']:
    sys.exit('Invalid input')

try:
    image = Image.open(sys.argv[1])

except FileNotFoundError:
    sys.exit('Input does not exist')

shirt = Image.open('shirt.png')

image = ImageOps.fit(image, size=shirt.size)

image.paste(shirt, shirt)

image.save(sys.argv[2])
