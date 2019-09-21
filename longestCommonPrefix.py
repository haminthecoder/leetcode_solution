# Python version 3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = 0
        shortest_str = ""
#         First find shortest length 

        if not strs:
            return ""
        
        shortest_str = min(strs,key=len)

        # When finding shortest str via this method I got an 
        # Index out of range error

        # for word in strs:
        #     if shortest == 0 or shortest > len(word):
        #         shortest = len(word)
        #         shortest_str = word
                
        
        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        
        return shortest_str
        