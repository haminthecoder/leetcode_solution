def solution(A):
    # write your code in Python 3.6
    if len(A) == 0 or len(A) == 1:
        return 0
        
    def flip(N):
        if N == 1:
            N = 0
        else:
            N = 1
        return N
        
    def count_flip(arr, prev):
        count = 0
        while arr:
            curr = arr.pop(0)
            if prev == curr:
                count += 1
                curr = flip(curr)
            prev = curr
        return count
    
    if len(A) == 0 or len(A) == 1:
        return A

    copy = A.copy()
    prev = copy.pop(0)
    # Num flips when first index = A[0]
    count = count_flip(copy,prev)

    # Num flips when first index = flip(A[0])
    prev = flip(A.pop(0))
    rev_count = 1 + count_flip(A, prev)
    
    return min(count,rev_count)
            
            

            
