# Find the minimum coins required for S from given list of coins.
# Solve using Dynamic Programming


def min_coin(S, coins):
    minv = [99999999] * (S + 1)
    minv[0] = 0
    for i in range(1, S + 1):
        for j in range(len(coins)):
            if coins[j] <= i and (minv[i - coins[j]] + 1) < minv[i]:
                minv[i] = minv[i - coins[j]] + 1
    print "Minimum coins for sum of %d required is %d using %s coins" % (S, minv[S], coins)


if __name__ == "__main__":
    S = 11
    coins = [1, 2, 5]
    min_coin(S, coins)
