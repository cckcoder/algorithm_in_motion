def fib(number):
    if number == 1 or number == 2:
        return 1
    else:
        fib_num = (number - 1) + (number - 2)
        print(f"{number - 1} + {number - 2} = {fib_num}")
        return fib(number - 1) + fib(number - 2)


print(fib(10))
