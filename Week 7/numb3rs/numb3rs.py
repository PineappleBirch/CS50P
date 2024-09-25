import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    number = r'(2[0-4]\d|25[0-5]|1?\d{1,2})'
    if _ := re.search(fr'^{number}\.{number}\.{number}\.{number}$', ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
