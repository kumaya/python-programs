# Zeckendorf's theorem states that every positive integer can be written uniquely as a sum of distinct non-neighbouring
# Fibonacci numbers. Two Fibonacci numbers are neighbours if they one come after other in Fibonacci Sequence
# (0, 1, 1, 2, 3, 5, ..). For example, 3 and 5 are neighbours, but 2 and 5 are not.


def greatest_nearest_fib(n):
    if n <= 0:
        return -1
    a = 0
    b = 1
    c = a + b
    while c <= n:
        a = b
        b = c
        c = a + b
    return b


def int_representation(n):
    if n < 1:
        return
    while n > 0:
        rep = greatest_nearest_fib(n)
        print rep
        n -= rep


if __name__ == "__main__":
    nth = 7
    int_representation(nth)