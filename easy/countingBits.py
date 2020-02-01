class Solution:
    def countBits(self, num: int) -> List[int]:
        def countNumBits(num):
            num_bits = 0
            while num:
                num_bits += num & 1            
                num >>= 1
            return num_bits
        result = []
        for i in range(num+1):
            result.append(countNumBits(i))
        
        return result
            
        