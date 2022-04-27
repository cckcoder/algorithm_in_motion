import sys


def factorization(n):
    original_number = n
    factor = []
    i = 2
    while n >= i:
        if n % i == 0:
            n /= i
            factor.append(i)
            i = 1
        i += 1
    print(original_number, "=", end=" ")
    print(*factor, sep="*")


if __name__ == "__main__":
    args = sys.argv
    if len(args):
        factorization(int(args[1]))
