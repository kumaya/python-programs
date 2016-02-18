# Given a input string
# rearrange to form palindrome
# return palindromic string or -1 if palindrome is not possible


def rearrange_to_palindrome(inp):
    d = {}
    len_inp = len(inp)
    # Base case
    if inp is None or len_inp < 2:
        return -1

    # Create dictionary containing occurances in input
    for i in inp:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1

    # return if occurance of more than one key is once
    one_occurance = 0
    odd_occurance = 0
    for i in d.values():
        if i == 1:
            one_occurance += 1
        if i%2 != 0:
            odd_occurance += 1
        if one_occurance > 1 or odd_occurance > 1:
            return -1

    # rearrange to form palindrome
    s = []
    for string, count in d.items():
        if count % 2 != 0:
            mid = string

        j = count/2
        while j > 0:
            s.append(string)
            s.insert(0, string)
            j -= 1

    # For leftover odd string
    middle = len_inp/2
    s.insert(middle, mid)

    return "".join(s)


if __name__ == "__main__":
    num = "12344342551"
    print num, rearrange_to_palindrome(num)