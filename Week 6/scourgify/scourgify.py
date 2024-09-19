import csv
import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

try:
    with open(sys.argv[1]) as input_file, open(sys.argv[2], 'w') as output_file:
        reader = csv.DictReader(input_file)
        writer = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])

        writer.writeheader()
        
        for row in reader:

            last, first = row['name'].split(sep=', ')
            house = row['house']

            writer.writerow({'first': first, 'last': last, 'house': house})

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')





