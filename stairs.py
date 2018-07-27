# recursive staircase problem!

# recursive
def ways(n, memo):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = ways(n-1, memo) + ways(n-3, memo) + ways(n-5, memo)
        return memo[n]


# iterative
def waysI(n, x):
    if n == 0:
        return 1
    memo = [0] * (n+1)
    memo[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in x:
            if i-j >= 0:
                total += memo[i-j]
        memo[i] = total
    return memo[n]


if __name__ == "__main__":
    n = 41
    memo = [-1] * (n+1)
    print "Number of ways you can climb", n, "stairs:", ways(n, memo)
    print "ITERATIVE: Number of ways you can climb", n, "stairs:", waysI(n, {1,3,5})

    from timeit import Timer

    a = 512
    bs = Timer("ways(a, [-1]*(a+1))",
               "from __main__ import ways, a")
    print "time taken for ways: ", bs.timeit(number=100000), "sec"
    bs = Timer("waysI(a, {1,3,5})",
               "from __main__ import waysI, a")
    print "time taken for waysI: ", bs.timeit(number=100000), "sec"
