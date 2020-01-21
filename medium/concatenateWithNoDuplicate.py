# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    ans = 0
    for i in range(len(A)):
        for j in range(len(A)):
            new_word = ''
            if i != j:
                new_word = A[i] + A[j]
                if len(new_word) == len(set(new_word)):
                    if len(new_word) > ans:
                        ans = len(new_word)
        tmp = ''
        for k in range(0, j):
            if i != k:
                tmp += A[k]
            new_word = A[i] + tmp
            if len(new_word) == len(set(new_word)):
                if len(new_word) > ans:
                    ans = len(new_word)
                        
    return ans
                
