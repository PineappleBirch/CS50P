def main():
    x = convert(input("What time is it? "))

    if x <= 8 and x >= 7:
        print("breakfast time")
    elif x <= 13 and x >= 12:
        print("lunch time")
    elif x <= 19 and x >= 18:
        print("dinner time")


def convert(time):
    x, y = time.split(":")
    x, y = int(x), int(y)
    x *= 60
    return (x + y)/60


if __name__ == "__main__":
    main()
