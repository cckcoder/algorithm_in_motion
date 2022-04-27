def show_fruit():
    fruits = []
    break_point1 = True

    while True:
        fruit = input(">")
        if fruit == "end":
            break
        else:
            fruits.append(fruit)

    while True:
        words = input(">")
        if words == "end":
            break
        else:
            for fruit in fruits:
                if fruit.startswith(words):
                    print(fruit)


if __name__ == "__main__":
    show_fruit()
