class Solution:
#     def reverseWords(self, s: str) -> str:
# #         words = s.split(" ")
# #         result = ""
        
# #         for i in range(len(words)):
# #             if i == len(words) - 1:
# #                 result += words[len(words) - i - 1]
# #             else:
# #                 result += words[len(words) - i - 1] + " "


        
# #         return result
#         return (" ".join(s.split()[::-1]))
    
    def reverseWords(self, s):
        result = ""
        for i in range(len(s)):
            result += s[len(s) - i - 1]
        print(result)
        
        return result



if __name__ == "__main__":
    solution = Solution()
    solution.reverseWords('hello')

            
        