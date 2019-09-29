# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word in the string.
# If the last word does not exist, return 0.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None:
            return 0
        
        words = s.split()
        
        if words:
            return len(words[-1])
        else:
            return 0
        
        
        