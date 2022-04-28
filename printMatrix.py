
m = [[ 1, 4, -2],
     [-2, 3,  4],
     [ 3, 1,  3]]

print "print diagnonally from start:"
for i in range(len(m)):
    for j in range(i+1):
        print m[i-j][j],
for i in range(len(m[0])-1):
    k = len(m) - 1
    for j in range(i+1, len(m[0])):
        print m[k][j],
        k -= 1

print ""
print "print diagnonally from end:"
for i in range(len(m[0]), 0, -1):
    k = len(m)-1
    for j in range(i, len(m[0])):
        print m[k][j],
        k -= 1
for i in range(len(m)-1, -1, -1):
    for j in range(i,-1, -1):
        print m[j][i-j],