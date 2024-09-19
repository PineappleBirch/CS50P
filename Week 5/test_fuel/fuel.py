def main():
    while True:
        try:
            fuel = input("Fraction: ")
            output = convert(fuel)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(output))


def convert(fraction):
    fuel_list = fraction.split("/", maxsplit=1)
    x = int(fuel_list[0])
    y = int(fuel_list[1])
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round((x / y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
