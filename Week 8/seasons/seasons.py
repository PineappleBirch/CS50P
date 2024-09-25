from datetime import date, datetime
import inflect
import sys


def main():

    try:
        date_of_birth = datetime.strptime(input('Date of Birth: '), '%Y-%m-%d').date()

    except ValueError:
        sys.exit('Invalid date')

    today = date.today()

    age = today - date_of_birth
    
    age_minutes = int(to_minutes(age))

    print(f'{verbalize(age_minutes).capitalize()} minutes')


def to_minutes(age):

    return (age.total_seconds()) / 60


def verbalize(age):

    p = inflect.engine()

    return p.number_to_words(age, andword='')



if __name__ == "__main__":
    main()
