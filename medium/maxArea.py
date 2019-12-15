class Solution:
    # Time limit exceeded
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        for i in range(len(height)):
            areas = []
            for j in range(i, len(height)):
                area = (j-i) * min(height[i],height[j])
                areas.append(area)
            if max(areas) > maximum:
                maximum = max(areas)
        return maximum
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        lo, high = 0, len(height) - 1
        
        while lo < high:
            maximum = max(maximum, (high-lo) * min(height[lo], height[high]))
            if height[lo] < height[high]:
                lo += 1
            else:
                high -= 1
        return maximum
    