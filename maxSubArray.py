#Kadane's Algorithm
#Program to find maximum sub array in an array

class maxSubArray:
    def __init__(self, inpArr):
        self.inpArr = inpArr

    def findMaxSubArray(self):
        maxSum = 0
        currentSum = 0
        currentEnd = 0
        currentStart = 0
        maxEndIndex = 0
        maxStartIndex = 0
        while (currentEnd < len(self.inpArr)):
            currentSum += self.inpArr[currentEnd]
            if (currentSum > maxSum):
                maxSum = currentSum
                maxStartIndex = currentStart
                maxEndIndex = currentEnd
            if (currentSum < 0):
                currentSum = 0
                currentStart = currentEnd + 1
            currentEnd += 1
        print ("maxSum: {0} \nmaxStartIndex: {1} \nmaxEndIndex: {2}".format(maxSum, maxStartIndex, maxEndIndex))
        print self.inpArr[maxStartIndex:maxEndIndex+1]

if __name__:
    inpArr = [1, 2, 3, -90, 6, 7, -2, 10,-123, 12]
    #inpArr = [-2, 4, -2, 7, 4, -8, -6, 2, 9, 1, 0, -4]
    obj = maxSubArray(inpArr)
    obj.findMaxSubArray()