class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        for i in range(len(nums)):
            mid = (low + high) // 2 # // Operator => round up or down
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

                
        