# MegaCorp wants to give bonuses to its employees based on how many lines of
# codes they have written. They would like to give the smallest positive amount
# to each worker consistent with the constraint that if a developer has written
# more lines of code than their neighbor, they should receive more money.
#
# Given an array representing a line of seats of employees at MegaCorp,
# determine how much each one should get paid.
#
# For example, given [10, 40, 200, 1000, 60, 30],
# you should return [1, 2, 3, 4, 2, 1].


def ranking(n, arr):
    out = [1] * n
    # pass 1 from left to right
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            out[i] = out[i-1] + 1
    # pass 2 from right to left for correct ordering
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1] and out[i] <= out[i+1]:
            out[i] = out[i+1] + 1
        # elif arr[i] == arr[i+1] and out[i] == out[i+1]:
        #     out[i] = out[i + 1] + 1
    return out


if __name__ == '__main__':
    n = 6
    inp = [10, 40, 200, 1000, 60, 30]
    out_arr = ranking(n, inp)
    print out_arr
    assert out_arr == [1, 2, 3, 4, 2, 1]

    n = 10
    inp = [9, 2, 3, 6, 5, 4, 3, 2, 2, 2]
    print ranking(n, inp)
