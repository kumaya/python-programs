# fibonacci series
def fib(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1) + fib(n-2)

print "fibinacci series value : {}".format(fib(6)) # 0:1, 1:1, 2:2, 3:3, 4:5, 5:8, 6:13

a = 233
aa = str(233)
aaa = aa[2:]
aaaa = aa[:-1]

print aaa, aaaa, int(aaaa)+int(aaa)==26



# Find the position of number in fingers if counting is in following order
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40
1, 2, 3, 4, 5, 6, 7, 8, 9, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  2,  3,  4

i = 28
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2]	#lenOfArr arr = 18
pos = arr[(i % len(arr))-1]
print "Position of %d is %d" %(i, pos)


# Find maximum number of chocolates
# Input- @price: price of chocolates; @money: amount you have; @wd: wrapper discount (amount of empty wrapper reuired to get new chocolates)
price = 2
money = 6
wd = 2
choc = money/price
wrap = money/price
while wrap>=wd:
	eat = wrap/wd
	choc += eat
	wrap = wrap % wd
	wrap = wrap + eat
print "No. of chocolates bought: ", choc