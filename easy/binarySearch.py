import string
import re 

class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums)

        for i in range(len(nums)):
            mid = (low + high) // 2 # // Operator => round up or down
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

    def reverseOnlyLetters(self, S):
        alphabet = list(string.ascii_lowercase)
        word1 = "".join(re.findall("[a-zA-z]+", S))
        result = ""
        print(word1)
        for i in range(len(S)):
            if S[i] in alphabet:
                result += S[len(S) - i - 1]
            else:
                result += S[i]
        print(result)
        return result
                
        
        # for i in range()
    

if __name__ == "__main__":
    solution = Solution()
    solution.reverseOnlyLetters('hamdd99d--ccc')
        
        

                
        