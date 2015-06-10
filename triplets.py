#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#Note: Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c) The solution set must not contain duplicate triplets.

class triplets:
    def __init__(self, inpArr):
        self.inpArr = inpArr
    
    def removeDuplicate(self, tempInp):
        finalOutput  = []
        for x in tempInp:
            if x not in finalOutput:
                finalOutput.append(x)
        if len(finalOutput)==0:
            return "Empty"
        else:
            print "Final triplets where sum = 0:"
            return finalOutput
         
    def solution(self):
        finalOutput1  = []
        a = 0
        sortedInp = sorted(self.inpArr)
        for a,val in enumerate(sortedInp):
            b = a + 1
            c = len(sortedInp) - 1
            if sortedInp[c] < 0:
                break
            while (b < c):
                sumTriplet = sortedInp[a] + sortedInp[b] + sortedInp[c]
                if sumTriplet < 0:
                    b += 1
                elif sumTriplet > 0:
                    c -= 1
                else:
                    tempOutput = []
                    tempOutput.append(sortedInp[a])
                    tempOutput.append(sortedInp[b])
                    tempOutput.append(sortedInp[c])
                    finalOutput1.append(tempOutput)
                    b += 1
                    c -= 1
        finalOutput = self.removeDuplicate(finalOutput1)
        print finalOutput
                  
if __name__:
    inpArr = [1,6,0,2,0,-1,-1,4,-6]
#     inpArr = [1,2,3,4,0]
    obj = triplets(inpArr)
    obj.solution()