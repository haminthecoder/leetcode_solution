# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if len(S) == 0:
        return ""
    lo, hi = 0, len(S)-1
    S = list(S)
    while lo < hi:
        if S[lo] == '?' and S[hi] == '?':
            S[lo], S[hi] = 'a', 'a'
        elif S[lo] != '?'and S[hi] == "?":
            S[hi] = S[lo]
        elif S[hi] != '?' and S[lo] == "?":
            S[lo] = S[hi]
        else:
            if S[lo] != S[hi]:
                return "NO"
        lo += 1
        hi -= 1
    if S[lo] == "?":
        S[lo] = 'a'
        
    return "".join(S)
        
        
