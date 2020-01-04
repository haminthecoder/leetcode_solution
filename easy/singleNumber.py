class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        
        for item in nums:
            d[item] = d.get(item, 0) + 1
                
        for item in d:
            if d[item] == 1:
                return item
        
        