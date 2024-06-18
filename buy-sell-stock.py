"""
i denotes ith day; k denotes transactions and 0 or 1=stock in hand
base case:
    T[-1][k][0] = 0 (-1 day with k transactions and 0 stock in hand)
    T[-1][k][1] = -inf (-1 day with k transaction with 1 stock in hand is impossible)
    T[i][0][0] = 0 (ith day with 0 transactions and 0 stock in hand)
    T[i][0][1] = -inf (ith day with 0 transaction and 1 stock in hand is impossible)
recurrance relation:
    T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
    T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
"""
import math

# Buy sell 1, 1 transaction
def bs1(prices):
    t_i10 = 0
    t_i11 = -math.inf
    for price in prices:
        t_i10 = max(t_i10, t_i11+price)
        t_i11 = max(t_i11, -price)
    return t_i10

prices = [1,3,2,8,4,9]
print(bs1(prices))