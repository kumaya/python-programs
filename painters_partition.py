# You have to paint N boards of length {A0, A1, A2, A3 ... AN-1}. There are K
# painters available and you are also given how much time a painter takes to
# paint 1 unit of board. You have to get this job done as soon as possible under
# the constraints that any painter will only paint contiguous sections of board.


def isPossible(a, k, x):
    students = 1
    Tsum = 0
    for i in a:
        Tsum += i
        if Tsum > x:
            students += 1
            Tsum = i
        if students > k:
            return False
    return True

def minSum(a, k):
    start = 0
    end = sum(a)
    res = end + 1
    while start <= end:
        mid = (start+end) // 2
        if isPossible(a, k, mid):
            res = min(res, mid)
            end = mid - 1
        else:
            start = mid + 1
    return res


if __name__ == '__main__':
    # a = [12, 34, 67, 90]
    a = [640, 435, 647, 352, 8, 90, 960, 329, 859]
    k = 3
    print minSum(a, k)
