# Given an randomly arranged array. Find all the subsets (of any size) in the array so that
# the sum of elements in subset is exactly divisible by 7

# This example illustrates the basic usecase of itertools library

from itertools import combinations, chain

def test(inp):
	len_inp = len(inp)
	var = chain.from_iterable(combinations(inp, n) for n in range(len_inp+1))
	return var

inp = [1,2,3,4,5]
print filter((lambda x: len(x)>0 and sum(x)%7 == 0), list(test(inp)))