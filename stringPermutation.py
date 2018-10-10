# Write a program to print all permutations of a given string


def printString(l):
    s = "".join(l)
    return s


def permute(arr, l, r):
    if l == r:
        print printString(arr)
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l+1, r)
            arr[i], arr[l] = arr[l], arr[i]


if __name__ == "__main__":
    s = "abc"
    l = list(s)
    lens = len(s)
    permute(l, 0, lens-1)
