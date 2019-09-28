class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None:
            return 0
        
        words = s.split()
        
        if words:
            return len(words[-1])
        else:
            return 0
        
        
        