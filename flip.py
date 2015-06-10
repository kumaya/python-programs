# input FaceValue of coin, arr containing coins value
# output: minimum no. of coins required to meet FaceValue

def countMinCoinsRequired(faceValue, denominations, temp):
    minCoins = faceValue
    if faceValue in denominations:
        return 1
    else:
        for i in range(len(denominations)):
            if denominations[i] <= faceValue:
                numCoins = 1 + countMinCoinsRequired(faceValue-denominations[i], denominations, temp)
                if numCoins < minCoins:
                    minCoins = numCoins
    return minCoins

arr = [3]
faceValue = 14
table = [0]*faceValue
# print table
print "minimum coins: %d" % countMinCoinsRequired(faceValue, arr, table)


print "\n", "*"*80
print 12345 + 5432l #66666
print 84444 + 04444 #88888


# def count(faceValue, denominations=[]):
#     cachedVal = []
#     for i in range(faceValue):
#         for j in denominations:
#             if j <= i and cachedVal[i-j]+1<cachedVal[i]:
#                 cachedVal[i] = cachedVal[i-j] +1
#     return cachedVal[faceValue]


# print count(faceValue, arr)
print float(1234/2)

print "\n", "*"*80
import time
arr = [59, 634, 601, 730, 540]
start = int(round(time.time() * 1000))
# print start
arr1 = sorted(arr) # [1, 1, 2, 3, 8]
while len(arr1) > 0:
    print len(arr1)
    poped_val = arr1[0]
    while len(arr1) > 0 and poped_val >= arr1[0]:
        arr1.pop(0)
end = int(round(time.time() * 1000))
print "time taken: ", (end - start)


print "%.2f" %(4.0 + 2.3)
a = [4,4,4,3,2,1]
b = set(a)
for i in  sorted(b):
    print i

x = 1
y = 1
z = 1
N = 2
res = []
res = [[i,j,k] for i in xrange(x+1) for j in xrange(y+1) for k in xrange(z+1) if i+j+k != N]
print res
print ord('a')
a = ['a', 'b', 'c']
print a[::-1]


lst = [[7, 1, 0], [2, 2, 2]]
for i in lst:
    print ' '.join(map(str, i))

print "*"*80
for i in range(1,5): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print str(i)*i

print "$"*80
x = [-2, 1]
y = [2, -1]
A = complex(x[0], x[1])
B = complex(y[0], y[1])
print A+B, A-B, A*B, A/B

class test(object):
    def __init__(self, a, b):
        self.A = a
        self.B = B

    def sum(self):
        self.res = self.A + self.B
        print "deep", self.res
        if (self.res).real == 0 and (self.res).imag == 0:
            print "yaya"
        else:
            self.res1()

    def res1(self):
        if (self.res).real == 0:
            print "%.2fi" %((self.res).imag)
        elif (self.res).imag == 0:
            print "%.2f" %((self.res).real)
        elif (self.res).imag > 0:
            print "%.2f + %.2fi" %((self.res).real, (self.res).imag)
        else:
            print "%.2f - %.2f" %((self.res).real, abs((self.res).imag))


test(A,B).sum()

# print "*"*80
# N = 2
# width = len(format(N, 'b'))
# print width
# for i in xrange(1,N+1):
#     bini = format(i, 'b')
#     deci = str(i)
#     octi= format(i, 'o')
#     hexi = (format(i, 'x')).upper()
#     print deci.rjust(width), octi.rjust(width), hexi.rjust(width), bini.rjust(width)





