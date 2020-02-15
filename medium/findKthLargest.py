class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create min_heap of size k
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        # For remaining elements, check if number is greater than root of min_heap
        for num in nums[k:]:
            # If bigger, replace it
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]
        