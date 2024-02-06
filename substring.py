"""
Sliding Window Template:
start, end, uniqueCount = 0, 0, 0
freqDict = dict()
res = SOME_VAL
while end < len(s):
    // increase the count of s[end] in freqDict
    // maintain uniqeCount of chars
    while uniqueCount condition:
         update res to mind min
         increase s[start] to make valid/invalid
         modify uniqueCount
    update d to find maximum
"""

# find max
def longest_substring_with_k_unique(s, k):
    start, end, counter = 0, 0, 0
    freqDict = dict()
    res = 0
    val = set()
    while end < len(s):
        freqDict[s[end]] = freqDict.get(s[end], 0) + 1
        if freqDict[s[end]] == 1:
            counter += 1
        while counter > k:
            freqDict[s[start]] -= 1
            if freqDict[s[start]] < 1:
                counter -= 1
            start += 1
        if res <= end - start + 1:
            if res < end - start + 1:
                val = set()
            res = end - start + 1
            val.add(s[start:end + 1])
        end += 1
    return res, val

def min_window_substring(s, t):
    start, end, uniqueChars = 0, 0, 0
    freqDict = dict()
    minWinSS = ""
    minWinRes = 10000000
    # convert string t to freqDict
    for c in t:
        freqDict[c] = freqDict.get(c, 0) + 1
        if freqDict[c] == 1:
            uniqueChars += 1

    while end < len(s):
        if s[end] in freqDict:
            freqDict[s[end]] -= 1
            if freqDict[s[end]] == 0:
                uniqueChars -= 1
        while uniqueChars == 0:
            if minWinRes > end-start+1:
                minWinRes = end-start+1
                minWinSS = s[start:end+1]
            if s[start] in freqDict:
                freqDict[s[start]] += 1
                if freqDict[s[start]] > 0:
                    uniqueChars += 1
            start += 1
        end += 1
    return minWinSS


if __name__ == "__main__":
    s = "aabacbebebe"
    k = 3
    print(longest_substring_with_k_unique(s, k))
    print(min_window_substring("this is a test string", "tist"))
