'''
Note that this is a csvFile solution.
If you want to simply pass in a list, run a for loop on the input, and run the same logic
'''
# Written by : Hamin Lee 
import csv
import json

class Solution(object):
    def mostPopularByUniqueBuyer(self, csvFile):
        '''
        Given this(JSON formatted CSV) as input (assume that it is a text file(csv in my case) stored in your local machine), 
        write a program that reads the file, and computes the most popular products based on two ranking methods.

        (1) Based on the unique number of users who purchased each product

        :Constraints:
        You can assume that the input file is fairly small in size (less than 1M lines).
        user_id and product_id are both strings of length at most 10.
        quantity is a positive integer between 1 and 100.
        Each line is a valid JSON message and always contains three elements (user_id, product_id, and quantity).

        :param csvFile: A CSV File containing JSON information
        :type x: String

        :rtype: String
        '''
        # Create a ditionary
        resultDict = {}
        # Time complexity O(|N|) = O(|Number of JSON object|)
        with open(csvFile, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                # If key does exist add quantity to the key else create the key 
                # .get() => Time Complexity of O(1)
                if resultDict.get(eval(line[0])["product_id"]) != None:
                    resultDict[eval(line[0])["product_id"]] += 1
                else:
                    resultDict[eval(line[0])["product_id"]] = 1
        # Get the maximum valued key from resultDict
        # Time complexity O(|P|) = O(|Number of Products|)
        mostPopular = max(resultDict, key=resultDict.get)

        return "Most popular product(s) based on the number of purchasers: [%s]" % mostPopular

    
    def mostPopularByQuantitySold(self, csvFile):
        '''
        Given this(JSON formatted CSV) as input (assume that it is a text file(csv in my case) stored in your local machine), 
        write a program that reads the file, and computes the most popular products based on two ranking methods.

        (2) Based on the total quantity of each product sold.

        :Constraints:
        You can assume that the input file is fairly small in size (less than 1M lines).
        user_id and product_id are both strings of length at most 10.
        quantity is a positive integer between 1 and 100.
        Each line is a valid JSON message and always contains three elements (user_id, product_id, and quantity).

        :param csvFile: A CSV File containing JSON information
        :type x: String

        :rtype: String
        '''
        # Create a ditionary
        resultDict = {}
        # Time complexity O(|N|) = O(|Number of JSON object|)
        with open(csvFile, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                # If key does exist add quantity to the key else create the key 
                # .get() => Time Complexity of O(1)
                if resultDict.get(eval(line[0])["product_id"]) != None:
                    resultDict[eval(line[0])["product_id"]] += eval(line[0])['quantity']
                else:
                    resultDict[eval(line[0])["product_id"]] = eval(line[0])['quantity']
        
        # Get the maximum valued key from resultDict
        # Time complexity O(|P|) = O(|Number of Products|)
        mostPopular = max(resultDict, key=resultDict.get)

        return "Most popular product(s) based on the quantity of goods sold: [%s]" % mostPopular


if __name__ == "__main__":
    solution = Solution()
    # lst = [{"user_id" : "uid_1", "product_id" : "pid_1", "quantity" : 45}, {"user_id" : "uid_1", "product_id" : "pid_2", "quantity" : 1}, {"user_id" : "uid_2", "product_id" : "pid_2", "quantity" : 5}]
    
    # ================== Solution ========================================================================
    print(solution.mostPopularByUniqueBuyer('q2Data.csv'))
    # Output : Most popular product(s) based on the number of purchasers: [GXX]
    # Dictionary Output: {'5Y0': 687, 'AI7': 509, '2MI': 124, 'GXX': 908, 'F5H': 145}
    print(solution.mostPopularByQuantitySold('q2Data.csv'))
    # Output : Most popular product(s) based on the number of purchasers: [GXX]
    # Dictionary Output: {'5Y0': 34658, 'AI7': 26055, '2MI': 6080, 'GXX': 44895, 'F5H': 7397}


