dic = {'name1': 26, 'name2': 24, 'name3':202, 'name4': 1}

# Sort a dictionary on the basis of value.
# Return list of tuples in sorted order
print sorted(dic.items(), key=lambda x: x[1], reverse=False)

# Return list of keys in sorted order
print sorted(dic, key=lambda x: x[1])

print help(dic.get)

# Reverse the dictionary and sort
print sorted(zip(dic.values(), dic.keys()))

# Sort dictionary using operator
# Return list of tuples
from operator import itemgetter
print sorted(dic.items(), key=itemgetter(1))
print sorted(dic.items(), key=itemgetter(0))
print "*"*80

# Sort
for k, v in sorted(dic.items(), key=lambda (k,v): v):
    print k, v
