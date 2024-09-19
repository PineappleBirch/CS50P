import sys
from random import choice
from pyfiglet import Figlet

def main():

    figlet = Figlet()

    fontlist = figlet.getFonts()

    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")

    if len(sys.argv) == 3 and (sys.argv[1] not in ["-f", "-font"] or sys.argv[2] not in fontlist):
        sys.exit("Invalid usage")

    text = input("Input: ")

    if len(sys.argv) == 1:
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(text))

    else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))

main()
