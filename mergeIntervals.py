class Solution:
    def merge(self, intervals):
        result = []
        if len(intervals) == 0:
            return result
        intervals = sorted(intervals, key = lambda x: x[0])
        for item in intervals:
            # If current item's first index is smaller than last index's last number
            if result and item[0] <= result[-1][1] :
                result[-1][1] = max(item[1], result[-1][1])
            else:
                # If nothing in result or first elemnt is current item bigger than
                # result element
                result.append(item)
        return result
    def noConsecutiveAs(self, inputStr):
        '''
        :type inputStr: String
        :rtype: Integer
        '''
        counter = 0
        i = 0
        result = ""
        while i < len(inputStr):
            if i < len(inputStr) - 2:
                if inputStr[i] == 'a':
                    if 'aaa' == inputStr[i:i+3]:
                        return -1
                    if inputStr[i+1] == 'a':
                        i += 2
                    else:
                        result += 'a'
                        i += 1
                        counter += 1
                else:
                    if 'aaa' == inputStr[i:i+3]:
                        return -1
                    if 'aa' == inputStr[i:i+2]:
                        i += 2
                    elif inputStr[i+1] == 'a':
                        result += 'a'
                        counter += 1
                        i += 1
                    else:
                        result += 'aa'
                        counter += 2
                        i += 2
            else:
                if i == len(inputStr) + 1:
                    counter += 4

        print(counter, result)
                    



if __name__ == "__main__":
    solution = Solution()
    solution.noConsecutiveAs('heaaaallo')
