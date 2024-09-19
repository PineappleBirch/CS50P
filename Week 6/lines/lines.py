import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')

counter = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip()
            if not line.startswith('#') and line != "":
                counter += 1

        print(counter)

except FileNotFoundError:
    sys.exit('File does not exist')
