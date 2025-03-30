while True:
    new_str = input("Введіть значення з літерою 'H': ")
    index = 0
    while index < len(new_str):
        if new_str[index] in ("H", "h"):
            print(f"В веденому слові є літера \"H\"")
            break
        index += 1
    else:
        print(f"Будь ласка, введіть слово, в якому є літера 'H'")
        continue
    break