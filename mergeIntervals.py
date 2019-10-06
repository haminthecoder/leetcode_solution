class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if len(intervals) == 0:
            return result
        intervals = sorted(intervals, key = lambda x: x[0])
        for item in intervals:
            if result and item[0] <= result[-1][1] :
                result[-1][1] = max(item[1], result[-1][1])
            else:
                # If nothing in result or first elemnt is current item bigger than
                # result element
                result.append(item)
        return result

