class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = True
        
        num = str(x)
        
        for i in range(len(num)):
            if num[i] != num[len(num) - i -1]:
                result = False
                
        return result
        