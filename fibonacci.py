# fibonacci using recursion
# Time complexity : O(2^n)


def fibonacci_using_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_using_recursion(n-1) + fibonacci_using_recursion(n-2)

# fibonacci usign dynamic programming
# Time complexity: O(n)


def fibonacci_using_dp(n):
    if dp[n] != -1:
        return dp[n]
    if n == 0:
        dp[n] = 0
    elif n == 1:
        dp[n] = 1
    else:
        dp[n] = fibonacci_using_dp(n-1) + fibonacci_using_dp(n-2)
    return dp[n]


if __name__ == "__main__":
    n = 20
    print("fibonacci for %sth number using fibonacci_using_recursion is %s" % (n, fibonacci_using_recursion(n)))
    dp = [-1] * (n+1)
    print ("fibonacci for %sth number using fibonacci_using_dp is %s" % (n, fibonacci_using_dp(n)))
    print ("*"*80)
    from timeit import Timer
    fur = Timer("fibonacci_using_recursion(n)", "from __main__ import fibonacci_using_recursion, n")
    print "time taken for fibonacci_using_recursion: ", fur.timeit(number=1000), "sec"
    fudp = Timer("fibonacci_using_dp(n)", "from __main__ import fibonacci_using_dp, n")
    print "time taken for fibonacci_using_dp: ", fudp.timeit(number=1000), "sec"