# Given an integer representing a given amount of change, write a
# function to compute the total number of coins required to make
# that amount of change. You can assume that there is always a
# 1 coin

from datetime import datetime


def minCoinsRec(change, coins):
    if change == 0:
        return 0
    tot_min_coins = 10000000
    for coin in coins:
        if change-coin >= 0:
            this_min_coins = minCoinsRec(change-coin, coins)
            if this_min_coins < tot_min_coins:
                tot_min_coins = this_min_coins
    return tot_min_coins + 1


def minCoinsTopDownDP(change, coins, dp):
    if change == 0:
        return 0
    if dp[change] != -1:
        return dp[change]
    tot_min_coins = 99999999
    for coin in coins:
        if change-coin >= 0:
            this_min_coins = minCoinsTopDownDP(change - coin, coins, dp)
            if this_min_coins < tot_min_coins:
                tot_min_coins = this_min_coins
    dp[change] = tot_min_coins + 1
    return dp[change]


def minCoinsBottomUpDP(change, coins, dp):
    dp[0] = 0
    for i in range(1, change+1):
        for coin in coins:
            if i-coin >= 0:
                curr_min_coins = dp[i-coin] + 1
                if curr_min_coins < dp[i]:
                    dp[i] = curr_min_coins
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
