grocery = {}

while True:
    try:
        new_item = input("").upper()
        grocery[new_item] += 1
        continue

    except KeyError:
        grocery[new_item] = 1
        continue

    except EOFError:
        for item in sorted(grocery):
            print(f"{grocery[item]} {item}")
        break
