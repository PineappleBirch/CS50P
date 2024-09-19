while True:
    try:
        fuel = input("Fraction: ")
        fuel_list = fuel.split("/", maxsplit=1)
        x = int(fuel_list[0])
        y = int(fuel_list[1])
        if x > y:
            continue
        output = x / y
        break
    except (ValueError, ZeroDivisionError, IndexError):
        continue

if output >= 0.99:
    print("F")
elif output <= 0.01:
    print("E")
else:
    print(f"{round(output * 100)}%")
