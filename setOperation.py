# set operation in list
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

# Return an array containing all elements of both array
print list(set(l1).union(l2))

# Return an array containing common elements of both array
print list(set(l1).intersection(l2))

# Return an array containing all elements of first array which are not in second
print list(set(l1).difference(l2))

# Return an array containing unique elements of both array
print list(set(l2).difference(l1).union(set(l1).difference(l2)))