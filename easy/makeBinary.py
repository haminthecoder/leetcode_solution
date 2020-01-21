# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    res = A * B
    binary = format(res, 'b')
    count = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            count += 1
        
    return count
