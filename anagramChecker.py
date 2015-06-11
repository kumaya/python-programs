# Program to check if two given strings are anagram in O(n) time

def anagramChecker(str1, str2):
	lst1 = [0] * 26
	lst2 = [0] * 26

	for i in xrange(len(str1)):
		pos = ord(str1[i]) - ord('a')
		lst1[pos] = lst1[pos] + 1

	for i in xrange(len(str2)):
		pos = ord(str2[i]) - ord('a')
		lst2[pos] = lst2[pos] + 1

	j = 0
	is_cool = True
	while  j<26 and is_cool:
		if lst1[j] == lst2[j]:
			j += 1
		else:
			is_cool = False

	return is_cool

if __name__ == "__main__":
	str1 = 'kuchbhi'
	str2 = 'bukihch'
	print anagramChecker(str1, str2)