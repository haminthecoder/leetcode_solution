class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        
        for i in range(len(A)):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False
        