class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for item in digits:
            num += str(item)
        num = int(num)
        num += 1
        num = str(num)
        
        return list(num)
        