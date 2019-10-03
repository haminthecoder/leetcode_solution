class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            newPerm = []
            for perm in result:
                for i in range(len(perm) + 1):
                    newPerm.append(perm[:i] + [num] + perm[i:])
            result = newPerm
            
        return result