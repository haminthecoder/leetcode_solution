class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
#         flag = False
#         index = 0
#         if len(needle) == 0:
#             return 0
        
#         for j in range(len(haystack)):
#             if haystack[j] == needle[0]:
#                 index = j
#                 for i in range(len(needle)):
#                     if haystack[j+i] == needle[i]:
#                         flag = True
#                     else:
#                         flag = False
                        
#         if flag is True:
#             return index
#         else:
#             return -1
                    
        
        