
for i in xrange(1, 5):
	print (1-10**i)/(1-10) * i
a =(0,0)
b=(0,10)

import itertools
a = 3
b = 1
c = 2
stuff = [a,b,c]
for L in xrange(len(stuff)+1):
  for subset in itertools.combinations(stuff, L):
    print subset

print "*"*80
inp = map(int, raw_input().split())
maxtopics = 0
guyslist = []
smarteams = 0
for _ in xrange(inp[0]):
    guyslist.append(raw_input())
for i in xrange(0, inp[0]-1):
    for j in xrange(i+1, inp[0]):
        knowntopics = 0
        for q in xrange(0, inp[1]):
            if (int((guyslist[i][q])) or int((guyslist[j][q]))):
                knowntopics += 1
        if knowntopics == maxtopics:
            smarteams += 1
        elif knowntopics > maxtopics:
            maxtopics = knowntopics
            smarteams = 1
print maxtopics
print smarteams