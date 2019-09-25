class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # ----------- Without making a copy --------------
        length = 1
        if len(nums) == 0:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[length] = nums[i]
                length += 1
        return length
        
# ----------- With making a copy --------------
# #         Create a result list
#         result = []
# #     Create a index counter for result list
#         i = 0
# #     If nums is not empty append the first element
#         if len(nums) != 0:
#             result.append(nums[0])
# #     Iterate through nums
#         for j in range(len(nums)):
# #         If current index is not in result array, append to result array
#             if result[i] != nums[j]:
#                 result.append(nums[j])
#                 i += 1
# #       Return the length of the result
#         nums = result
#         return len(result)
            
        

