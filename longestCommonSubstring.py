
def sorted_suffix_array(s):
    out = list()
    # O(n)
    for i in range(len(s)):
        out.append(s[i:])
    # O(log(n))
    print(sorted(out))
    return sorted(out)


def longest_common_substring(sa=[]):
    result = ""
    # O(n)
    for i in range(len(sa)-1):
        temp = ""
        for j, k in zip(sa[i], sa[i+1]):
            if j != k:
                break
            temp += j
        # print("== ", temp, "++ ", result)
        if len(temp) > len(result):
            result = temp
    return result


if __name__ == "__main__":
    s1 = "abcba"
    s2 = "cbadl"
    # TODO: add sliding window to remove same string considered multiple times.
    print(longest_common_substring(sorted_suffix_array(s1+"#"+s2+"%")))
