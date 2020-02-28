class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        x, y = bin(x), bin(y)
        x, y = list(x), list(y)
        
        x.pop(x.index('b')), y.pop(y.index('b'))
        print(x,y, type(x[0]), type(y))

        diff = abs(len(x)-len(y))
        if (len(x) < len(y)):
            tmp = list(reversed(x))
            for i in range(diff):
                tmp.append(str(0))
            x = list(reversed(tmp))
            
        if (len(x) > len(y)):
            tmp = list(reversed(y))
            for i in range(diff):
                tmp.append(str(0))
            y = list(reversed(tmp))
        
        
        for i in range(len(x)):
            if x[i] != y[i]:
                result += 1
        return result
        