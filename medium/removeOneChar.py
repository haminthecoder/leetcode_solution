# Written by : Hamin Lee 

class Solution(object):
    def equalsWhenOneCharRemoved(self, x, y):
        '''
        Implement a function/method that is given two strings and returns 
        whether one can be obtained by the other after removing exactly one character. 
        Specifically, given two strings x and y, return true if and only 
        if (1) x can be obtained by removing one character from y and/or 
        (2) if y can be obtained by removing one character from x.

        :param x: A non-empty string containing English letters only
        :type x: String

        :param y: A non-empty string containing English letters only
        :type y: String

        :rtype: Boolean
        '''
        # If len(x) and len(y) differs not exactly by 1, return False
        if (abs(len(x) - len(y)) != 1) :
            return False
        
        # Loop through shorter string
        shorterLen = min(len(x), len(y))
        counter = 0
    
        # Time Complexity of O(min(|len(A)| or |len(B)|)) == O(shorterLen)
        # xrange uses only 40 Bytes of memory 
        for i in xrange(shorterLen):
            if x[i] != y[i]:
                # If different increment counter by 1
                counter += 1
                # If x is the longer string compare x[i+1:] to y[i:] vice versa
                # This will check if we remove current index, the strings will match or not
                if len(x) > len(y):
                    if x[i+1:] == y[i:]:
                        return True
                    else:
                        return False
                if len(x) < len(y):
                    if x[i:] == y[i+1:]:
                        return True
                    else:
                        return False
        # If all elements are equal, then we simply have to remove the last element
        # Thus, return True
        if counter == 0:
            return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.equalsWhenOneCharRemoved("abb","aacb"))              # Returns False
    print(solution.equalsWhenOneCharRemoved("bcb","bb"))                # Returns True
    print(solution.equalsWhenOneCharRemoved("","bb"))                   # Returns False
    print(solution.equalsWhenOneCharRemoved("bcb","bb"))                # Returns True
    print(solution.equalsWhenOneCharRemoved("bb","cbb"))                # Returns True
    print(solution.equalsWhenOneCharRemoved("moloco","mocco"))          # Returns False
