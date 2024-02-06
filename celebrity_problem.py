

m = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
n = 4

def foo(m, n):
    inDeg = [0 for _ in range(n)]
    outDeg = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            outDeg[i] += m[i][j]
            inDeg[j] += m[i][j]
    print(inDeg, outDeg)
    for i in range(n):
        if inDeg[i] == n-1 and outDeg[i] == 0:
            print(i)
            return
    print(-1)

def bar(m, n):
    i = 0
    j = n-1
    c = -1
    while i<j:
        if m[i][j] == 1:
            i += 1
        else:
            j -= 1
    candidate = i
    for i in range(n):
        if i != candidate:
            if m[candidate][i] == 1 or m[i][candidate] == 0:
                print(-1)
                return
    print(candidate)


foo(m, n)
bar(m,n)