class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # [2,0,2,1,1,0] => [0, 0, 1, 1, 2, 2]
        # 0 - red 1 -white 2- blue
        # [] => []
        # bubble sort
        # i from 0 to len(nums)-1
        # j form 1 to len(nums) -1 -j
        # if list[i] > list[j] => swap
        # O(n^2) => space=>O(1)
        # [2,1,0]
        # i = 1 
        
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[j-1] > nums[j]:
        #             nums[j-1], nums[j] = nums[j], nums[j-1]
        # return nums
        
        # count => redCount, bCount, wCount
        # stack.pop() count++
        # []
        # [] += [0] * redCount 
        # O(n)
        rCount, wCount, bCount = 0, 0, 0
        while nums:
            tmp = nums.pop()
            if tmp == 0:
                rCount += 1
            elif tmp == 1:
                wCount += 1
            elif tmp == 2:
                bCount += 1
        
        nums += [0] * rCount
        nums += [1] * wCount
        nums += [2] * bCount
        return nums