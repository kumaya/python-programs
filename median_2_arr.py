def getMedian(a1, a2, n):
    if n == 0:
        return -1
    elif n == 1:
        return (a1[0] + a2[0]) / 2
    elif n == 2:
        return (max(a1[0], a2[0]) + min(a1[1], a2[1])) / 2
    else:
        m1 = median(a1, n)
        m2 = median(a2, n)
        if m1 > m2:
            if n%2==0:
                a1 = a1[:(n/2)+1]
                a2 = a2[(n/2)-1:]
                n = (n/2)+1
                return getMedian(a1, a2, n)
            else:
                a1 = a1[:(n/2)+1]
                a2 = a2[n/2:]
                n = (n/2)+1
                return getMedian(a1, a2, n)
        else:
            if n%2==0:
                a1 = a1[(n/2)-1:]
                a2 = a2[:(n/2)+1]
                n = (n/2)+1
                return getMedian(a1, a2, n)
            else:
                a1 = a1[n/2:]
                a2 = a2[:(n/2)+1]
                n = (n/2)+1
                return getMedian(a1, a2, n)

def median(a, n):
    if n % 2 == 0:
        return (a[n/2] + a[n/2 - 1])/2
    else:
        return a[n/2]


if __name__ == '__main__':
    a1 = [1, 2, 3, 6]
    a2 = [4, 6, 8, 10]
    n = len(a1)
    print getMedian(a1, a2, n)
