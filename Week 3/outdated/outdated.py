months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    user_input = input("Date: ").strip()

    try:
        month, day, year = user_input.split("/", maxsplit=3)

        month, day = int(month), int(day)

    except ValueError:

        try:
            temp_list = user_input.split(",", maxsplit=2)
            month, day = temp_list[0].split(" ", maxsplit=2)
            year = temp_list[1].lstrip()

            month = month.title()
            index = 0
            for item in months:
                index += 1
                if item == month:
                    month = index

            day = int(day)

        except ValueError:
            continue

    if 0 < month < 13 and 0 < day < 32:
        break

print(f"{year}-{month:02}-{day:02}")
