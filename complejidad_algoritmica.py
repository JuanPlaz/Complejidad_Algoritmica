import time
import sys

def factorial(n):
    response = 1

    while n > 1:
        response = response * n
        n = n - 1

    return response


def factorial_recursive(n):
    if n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    n = 9989
    sys.setrecursionlimit(n + 10)

    startingTime = time.time()
    #print(startingTime)
    factorial(n)
    endTime = time.time()
    #print(endTime)
    print(f"Execution time with bucle:\t{endTime - startingTime}");

    startingTime2 = time.time()
    #print(startingTime2)
    factorial_recursive(n)
    endTime2 = time.time()
    #print(endTime2)
    print(f"Execution time with recursive:\t{endTime2 - startingTime2}");