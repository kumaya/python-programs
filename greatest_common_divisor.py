# Program to find greatest common divisor
def GCD(a,b):
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b%a, a
    return b

def GCD_list(list):
    return reduce(GCD, list)

if __name__ == "__main__":
    N = 2
    for _ in xrange(N):
        len_arr = 42
        arr = [57670, 11531, 63401, 57490, 42367, 78497, 50839, 11006, 78160, 31714, 39422, 55944, 16087, 58737, 95643, 80183, 14398, 76300, 91732, 40558, 56759, 37801, 70584, 31594, 84096, 80732, 20257, 37857, 21118, 69229, 467, 55714, 16163, 40100, 49468, 64633, 30409, 29535, 5652, 63401, 32405, 97463]
        arr = sorted(arr)
        for i in arr:
            if arr.count(i) > 1 or len_arr <= 1:
                print "NO"
                break
        print GCD_list(arr)
