# decode strings
# Given 'a'='1', 'b'='2'.....'z'='26'
# decode number of ways a string can be represented into.
# like ways('13') = 2; since '13'='ac' or 'm'
# input = '123'; output = 3


def num_ways(inp, k):
    if k == 0:
        return 1
    s = len(inp) - k
    if inp[s] == '0':
        return 0

    result = num_ways(inp, k-1)
    if k >= 2 and int(inp[s:s+2]) <= 26:
        result += num_ways(inp, k-2)
    return result


def num_ways_dp(inp, k, memo):
    if k == 0:
        return 1
    s = len(inp) - k
    if inp[s] == '0':
        return 0
    # returning from memory here if already present
    if memo[k] != 0:
        return memo[k]
    result = num_ways_dp(inp, k-1, memo)
    if k >= 2 and int(inp[s:s+2]) <= 26:
        result += num_ways_dp(inp, k-2, memo)
    # adding to memory here
    memo[k] = result
    return result


if __name__ == "__main__":
    inp = "12345"
    k = len(inp)
    print "num_ways: ", num_ways(inp, k)
    memo = [0] * (k+1)
    print "num_ways_dp: ", num_ways_dp(inp, k, memo)

    from timeit import Timer
    a = "111111111111"
    bs = Timer("num_ways(a, len(a))",
               "from __main__ import num_ways, a")
    print "time taken for num_ways: ", bs.timeit(number=10000), "sec"
    bs = Timer("num_ways_dp(a, len(a), [0]*(len(a)+1))",
               "from __main__ import num_ways_dp, a")
    print "time taken for num_ways_dp: ", bs.timeit(number=10000), "sec"
