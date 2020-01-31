class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minDP = [nums[0]] + [float("-inf")] * (len(nums) -1)
        maxDP = [nums[0]] + [float("-inf")] * (len(nums) -1)
        res = nums[0]
        for i in range(1, len(nums)):
            minDP[i] = min(min((minDP[i-1] * nums[i]), (maxDP[i-1] * nums[i])), nums[i])
            maxDP[i] = max(max((minDP[i-1] * nums[i]), (maxDP[i-1] * nums[i])), nums[i])
            res = max(maxDP[i], res)
        
        return res