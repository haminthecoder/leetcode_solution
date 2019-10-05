# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(U, L, C):
    # write your code in Python 3.6
    '''
    sum of upper row = U
    sum of lower row = L
    sum of Kth column = C[k]
    '''
    rowLen = len(C)
    width, height = rowLen, 2 
    matrix = [[0 for x in range(width)] for y in range(height)] 
    
    for i in range(rowLen):
        if C[i] == 0:
            pass
        if C[i] == 1:
            currentFirstRowSum = 0
            currentSecondRowSum = 0
            for j in range(rowLen):
                currentFirstRowSum += matrix[0][j]
                currentSecondRowSum += matrix[1][j]
            if currentFirstRowSum < U:
                matrix[0][i] = 1
            if currentFirstRowSum == U and currentSecondRowSum < L:
                matrix[1][i] = 1
            if currentFirstRowSum == U and currentSecondRowSum == L:
                return "IMPOSSIBLE"
        if C[i] == 2:
            currentFirstRowSum = 0
            currentSecondRowSum = 0
            for j in range(rowLen):
                currentFirstRowSum += matrix[0][j]
                currentSecondRowSum += matrix[1][j]
            if currentFirstRowSum < U:
                matrix[0][i] = 1
            if currentSecondRowSum < L:
                matrix[1][i] = 1
            if currentFirstRowSum == U and currentSecondRowSum == L:
                return "IMPOSSIBLE"
    
    finalFirstRowSum = 0
    finalSecondRowSum = 0
    for j in range(rowLen):
        finalFirstRowSum += matrix[0][j]
        finalSecondRowSum += matrix[1][j]
    if finalFirstRowSum != U or finalSecondRowSum != L:
        return "IMPOSSIBLE"
    
    resultUpper = ""
    resultLower = ""
    
    for i in range(rowLen):
        resultUpper += str(matrix[0][i])
        resultLower += str(matrix[1][i])
    
    result = resultUpper + "," + resultLower
        
    return result

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

    

