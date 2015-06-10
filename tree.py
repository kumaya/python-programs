def GCD(a,b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b%a, a
    return b

def GCD_list(list):
    return reduce(GCD, list)

if __name__ == "__main__":
    N = input()
    for _ in xrange(N):
        len_arr = input()
        arr = map(int, raw_input().split())
        arr = sorted(arr)
        for i in arr:
            if arr.count(i) > 1 or len_arr <= 1:
                print "NO"
                break
        print GCD_list(arr)