import sys

class Solution:
    def reverse(self, x: int) -> int:
        prefix = 1
        result = ""
        
#       We have to consider edge case where input in in range but output is out of range
#       Thus we have to check if it overflows after we get the output
        INT_MAX = sys.maxsize  
        
#         # Check if integer overflows
#         if abs(x) > (1 << 31) - 1) :
#             return 0
        
        if x < 0 :
            prefix = -1
        
        num = abs(x)
        num = str(num)
        
        # String doesn't support item assignment
        # Thus c
        for i in range(len(num)):
            result += num[len(num)-i-1]
        
        result = int(result)
        
        if result > pow(2, 31):
            return 0
        else:
            return prefix * result
        
        
     
        