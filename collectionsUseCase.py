'''Use of collections library in python
'''

from collections import Counter, defaultdict

# Get the count of all unique elements in  a given string
inp = "12344652434cabck22732472468628426482469103013817932631702417492"
out_list = Counter(inp).most_common()
print out_list
print "Most frequently used element is %d and its count is %d" % (int(out_list[0][0]), out_list[0][1])

print "*"*80
# use case of default dictionary
inp = [('m', 5), ('a', 6), ('y', 4), ('a', 7), ('n', 8), ('k', 9)]
out_list = defaultdict(list)
for k, v in inp:
	out_list[k].append(v)
print out_list

out_list = defaultdict(float)
for k,v in inp:
	out_list[k] += v
print out_list

print "#"*80
# use case of namedtuple
'''A named tuple is just like a normal tuple, but it allows you to give names
to each position making the code more readable and self-documenting.
'''
from collections import namedtuple

inp = {'x': 30, 'y': 45}
coordinate = namedtuple('Coordinate', ['x', 'y'])
print coordinate(**inp)

inp = [1, 2]
val = coordinate._make(inp)
print val


print "%"*80
# Use case of ordered dictionary
'''OrderedDicts act just like regular dictionaries except they remember the
order that items were added.
'''
from collections import OrderedDict
my_ord_dict = OrderedDict()
my_ord_dict['a'] = 1
my_ord_dict['b'] = 2
my_ord_dict['c'] = 3

print "Ordered dictionary in normal order: "
for k in my_ord_dict:
	print k,

print "\nOrdered dictionary in reversed order"
for k in reversed(my_ord_dict):
	print k,

print ""
print my_ord_dict.popitem()
print my_ord_dict.items()
