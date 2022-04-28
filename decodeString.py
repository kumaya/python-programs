# given encoded input string, return decoded form
# Inp = 2[ab10[b]d]
# Out = "abbbbbbbbbbbdabbbbbbbbbbbd"

def decodeStr(inp):
    counts = []
    i = 0
    while i < len(inp):
        if inp[i].isdigit():
            count = 0
            while inp[i] != "[":
                count = count*10 + int(inp[i])
                i += 1
            if count > 0:
                counts.append(count)
        else:
            i += 1
    strStack = []
    for i in inp:
        if i == "]":
            tmp = []
            while strStack[-1] != "[":
                x = strStack.pop()
                tmp.append(x)
            strStack.pop()  # remove [
            count = counts.pop()
            # count = int(strStack.pop())
            tmp = tmp*int(count)
            strStack.append("".join(tmp[::-1]))
        elif not i.isdigit():
            strStack.append(str(i))
    return strStack[0]


if __name__ == '__main__':
    inp = "2[ab2[bc]d]"
    res = decodeStr(inp)
    print res
    assert res == "abbcbcdabbcbcd"
    inp = "2[a13[b]]"
    res = decodeStr(inp)
    print res
    assert res == "abbbbbbbbbbbbbabbbbbbbbbbbbb"
    inp = "2[a10[b]]"
    res = decodeStr(inp)
    print res
    assert res == "abbbbbbbbbbabbbbbbbbbb"