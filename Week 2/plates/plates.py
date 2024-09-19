def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def digit_in_middle(string):
    n = 0
    for char in string:
        if char.isalpha():
            n += 1
        elif char.isdigit():
            n += 1
            break
        
    if n == len(string):
        return False

    if not string[n:].isdigit():
        return True
    return False


def check_if_zero_first(string):
    for char in string:
        if char.isdigit():
            if char == "0":
                return True
            else:
                return False
    return False


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not (s[0:2].isalpha()):
        return False
    elif not s.isalnum():
        return False
    elif digit_in_middle(s):
        return False
    elif check_if_zero_first(s):
        return False
    return True

main()
