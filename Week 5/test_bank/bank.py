def main():

    greeting = input("Greeting: ")

    print(f'${value(greeting)}')

def value(greeting):

    greeting = greeting.strip().lower()

    if greeting.startswith('hello'):
        reward = 0

    elif greeting.startswith('h'):
        reward = 20

    else:
        reward = 100

    return reward


if __name__ == "__main__":
    main()
