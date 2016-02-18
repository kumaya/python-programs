# Given a compressed string in the format: a2b1ca; where given string means aabca
# Given Q test cases and corresponding k inputs
# find the kth alphabet in the sorted uncompressed string.
# If kth alphabet does not exist return -1

inp_str = raw_input()
len_str = len(inp_str)
hashed_str = {}
for i in xrange(len_str):
    if 92 <= ord(inp_str[i]) <= 117:
        n = 0
        j = i
        while (j + 1 <= len_str - 1 and 92 > ord(inp_str[j + 1])):
            n += 1
            j += 1
        temp = inp_str[i + 1:j + 1]
        if n == 0:
            temp = 1
        temp = int(temp)
        if inp_str[i] in hashed_str.keys():
            hashed_str[inp_str[i]] += int(temp)
        else:
            hashed_str[inp_str[i]] = int(temp)
    i = j
sorted_hashed_str = sorted(hashed_str.items(), key=lambda x: x[0])
print sorted_hashed_str

sum_vals = 0
for i in xrange(len(sorted_hashed_str)):
    sum_vals += sorted_hashed_str[i][1]
# print sum_vals

Q = input()
assert (1 <= Q <= 10 ** 5)
for _ in xrange(Q):
    k = input()
    assert (1 <= k <= 10 ** 18)
    x = 0
    i = 0
    if k > sum_vals:
        print -1
    else:
        while x < k:
            x += sorted_hashed_str[i][1]
            i += 1
        print sorted_hashed_str[i - 1][0]
