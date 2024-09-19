import random

while True:

    try:
        n = int(input("Level: "))

        if n < 1:
            continue

    except ValueError:
        continue

    break

answer = random.randint(1, n)

while True:

    try:
        guess = int(input("Guess: "))

    except ValueError:
        continue

    if guess < 1:
        continue

    if guess < answer:
        print("Too small!")
        continue

    elif guess > answer:
        print("Too large!")
        continue

    else:
        print("Just right!")
        break
