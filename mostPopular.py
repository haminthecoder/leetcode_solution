'''
Given this as input (assume that it is a text file stored in your local machine), 
write a program that reads the file, and computes the most popular products based on two ranking methods.

(1) Based on the unique number of users who purchased each product, and
(2) Based on the total quantity of each product sold.
'''
# Written by : Hamin Lee 

class Solution(object):
    def mostUniqueBuyer(self, lst):
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
        # Create a ditionary
        result = {}
        print(lst)
        for i in xrange(len(lst)):
            print(lst[i], 'Hello')

    
    # def mostPurchases(self, )


if __name__ == "__main__":
    solution = Solution()
    lst1  = [1,2,3,4]
    print(solution.mostUniqueBuyer(lst1))

