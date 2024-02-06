# https://leetcode.com/problems/combination-sum
def combination_sum(candidates, target, start, end, tmp, res):
    if target == 0:
        res.append(tmp[:])
        return
    if target < 0:
        return
    for i in range(start, end):
        if candidates[i] <= target:
            tmp.append(candidates[i])
            combination_sum(candidates, target-candidates[i], i, end, tmp, res)
            tmp.pop()

# https://leetcode.com/problems/combination-sum-ii/description/
def combination_sum2(candidates, target, start, end, tmp, res):
    if target == 0:
        res.append(tmp[:])
        return
    if target < 0:
        return
    for i in range(start, end):
        if target < candidates[i]:
            continue
        if candidates[i] == candidates[i-1] and i > start:
            continue
        tmp.append(candidates[i])
        combination_sum2(candidates, target-candidates[i], i+1, end, tmp, res)
        tmp.pop()

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    res = []
    combination_sum(sorted(candidates), target, 0, len(candidates), [], res)
    print(res)

    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = []
    combination_sum2(sorted(candidates), target, 0, len(candidates), [], res)
    print(res)
