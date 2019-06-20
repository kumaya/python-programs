# Given an integer representing a given amount of change, write a
# function to compute the total number of coins required to make
# that amount of change. You can assume that there is always a
# 1 coin

from datetime import datetime


def minCoinsRec(change, coins):
    if change == 0:
        return 0
    # total number of coins required to make change will not be greater then
    # the value of coin. So min equals change
    min = change
    for coin in coins:
        if change - coin >= 0:
            c = minCoinsRec(change - coin, coins)
            if min > c + 1:
                min = c + 1
    return min


def minCoinsTopDownDP(change, coins, dp):
    if change == 0:
        return 0
    if dp[change] != -1:
        return dp[change]
    min = change
    for coin in coins:
        if change-coin >= 0:
            c = minCoinsTopDownDP(change - coin, coins, dp)
            if min > c+1:
                min = c+1
    dp[change] = min
    return dp[change]


def minCoinsBottomUpDP(change, coins, dp):
    dp[0] = 0
    for i in range(1, change+1):
        for coin in coins:
            if i-coin >= 0:
                c = dp[i-coin] + 1
                if c < dp[i]:
                    dp[i] = c
    return dp[change]


if __name__ == '__main__':
    coins = [1, 2, 5]
    change = 31
    s = datetime.now()
    print "minimum coins with recursion: ", minCoinsRec(change, coins)
    e = datetime.now()
    print "total time taken using recursion: ", e-s

    dp = [-1] * (change+1)
    s = datetime.now()
    print "minimum coins with top down dp: ", minCoinsTopDownDP(change, coins, dp)
    e = datetime.now()
    print "total time taken using top down dp: ", e - s

    dp = [99999999] * (change+1)
    s = datetime.now()
    print "minimum coins with bottom up dp: ", minCoinsBottomUpDP(change, coins, dp)
    e = datetime.now()
    print "total time taken using bottom up dp: ", e - s
