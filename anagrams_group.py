# Group of anagrams. Given a list of strings return another list containing common anagrams

def anagram_list(strng):
	ar = [0]*26
	formatted_strng = strng.replace(' ', '')
	for ch in formatted_strng:
		pos = ord(ch.lower()) - ord('a')
		ar[pos] += 1
	return ar


def group_strns(td, list_str):
	final = []
	for st in list_str:
		temp =[]
		for st2 in list_str:
			if not cmp(td[st], td[st2]):
				temp.append(st2)
		if temp not in final:
			final.append(temp)
	return final


def main(list_str):
	temp_dict = {}
	for st in list_str:
		temp_dict[st] = anagram_list(st)
	print group_strns(temp_dict, list_str)


if __name__ == "__main__":
	list_str = ['pear','amleth','dormitory','tinsel','dirty room','hamlet','listen','silnet']
	main(list_str)
