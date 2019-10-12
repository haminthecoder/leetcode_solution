import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        required = math.floor(len(nums)/3) 
        numSet = list(set(nums))
        result = []
        
        for item in numSet:
            if nums.count(item) > required:
                result.append(item)
        return result
                
                