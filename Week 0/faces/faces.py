def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


def main():
    print(convert(input("")))


main()
