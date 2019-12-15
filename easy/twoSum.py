class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, 0
        
        resultDict = {}
#        Enumerate() works as (key,value) and takes (list, startingIdx) as input
        for key, value in enumerate(nums):
            tmp = target - value
            if tmp in resultDict:
                return [resultDict[tmp], key]
            else:
                resultDict[value] = key
    