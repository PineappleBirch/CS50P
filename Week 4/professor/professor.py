import random


def main():
    score = 0
    n = get_level()

    for _ in range(10):

        x = generate_integer(n)
        y = generate_integer(n)
        err_count = 0
        print(_)
        while True:

            print(f"{x} + {y} =", end=" ")

            answer = int(input())

            if answer == (x + y):
                score += 1
                break
            else:
                err_count += 1
                print("EEE")

                if err_count < 3:
                    continue
                else:
                    print(f"{x} + {y} = {x+y}")
                    break

    print(f"Score: {score}")


def get_level():

    while True:

        try:
            n = int(input("Level: "))

            if n in [1, 2, 3]:
                break
            else:
                continue

        except ValueError:
            continue
        
    return n



def generate_integer(level):

    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
