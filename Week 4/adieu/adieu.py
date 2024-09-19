import inflect

p = inflect.engine()

name_list = []

while True:

    try:
        uinput = input("Name: ")
        name_list.append(uinput)
        continue

    except EOFError:
        break

inflected_list = p.join(name_list)

print(f"Adieu, adieu, to {inflected_list}")
