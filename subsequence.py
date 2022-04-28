def subsequence(inp, s, out, count):
    if s == len(inp):
        count[0] = max(count[0], len(out))
        return
    for i in range(s, len(inp)):
        if len(out) > 0 and out[-1] >= inp[i]:
            count[0] = max(count[0], len(out))
            continue
        subsequence(inp, i+1, out+[inp[i]], count)


def subsequenceDP(nums):
    dp = [0]*len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        tmp = 0
        for j in range(0, i):
            if nums[i] > nums[j]:
                tmp = max(tmp, dp[j])
        dp[i] = tmp+1
    print dp
    return max(dp)


if __name__ == '__main__':
    inp = [10,9,2,5,3,7,101,18]
    # inp = [0,1,0,3,2,3]

    # inp = [7,7,7,7,7,7,7]
    # inp =[1,3,6,7,9,4,10,5,6]
    c = [0]
    subsequence(inp, 0, [], c)
    print c[0]

    print subsequenceDP(inp)