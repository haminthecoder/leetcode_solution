class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Solution using Recursion
        # Time Complexity: (O(|len(a)| + |len(b)| + carry)) 
        # Space Complexity: (O(|a| + |b|)) 

        # Base Case
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a

        # If Both last index of a and b are 1 
        if a[-1] == '1' and b[-1] == '1':
        # Nested Recursion because we need to generate "10"
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), "1") + "0"
        
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + "0"
        else:
            return self.addBinary(a[:-1], b[:-1]) + "1"

                    
            
        