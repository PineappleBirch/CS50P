import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r'iframe.+h.+youtube\.com/embed/([a-zA-Z0-9]{11}).+iframe', s):
        return f'https://youtu.be/{url[1]}'
    else:
        return None


if __name__ == "__main__":
    main()
