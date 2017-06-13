# given an unsorted array. return True if pythagorian triplets exists
# pythagorian triplets: a^2 + b^2 = c^2; (a,b,c) are pythagorian triplets

def pythaTrip(arr, lenArr):
	# square all elements. O(n)
	for i in range(lenArr):
		arr[i] = arr[i] * arr[i]
	# sort the array. O(nlog(n))
	arr = sorted(arr)
	# O(n^2)
	for k in range(lenArr-1, 1, -1):
		i = 0
		j = k-1
		while j > i:
			a = arr[i]
			b = arr[j]
			c = a + b
			if c == arr[k]:
				print a, b, c
				return True
			elif c > arr[k]:
				j -= 1
			else:
				i += 1
	return False

if __name__ == "__main__":
	arr = [1,4,2,3,5]
	lenArr = len(arr)
	print pythaTrip(arr, lenArr)