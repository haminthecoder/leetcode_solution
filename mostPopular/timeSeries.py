'''
Note that this is a csvFile solution.
If you want to simply pass in a list, run a for loop on the input, and run the same logic
'''
# Written by : Hamin Lee 
import csv

class Solution(object):
    def mostUniqueUsers(self, csvFile):
        '''
        Consider only the rows with country_id = "BDV" (there are 844 such rows). 
        For each siteID, we can compute the number of unique userID's found in these 844 rows. 
        Which siteID has the largest number of unique users? And what's the number?
        ts = [0]
        userID = [1]
        country_id = [2]
        siteID = [3]

        :param csvFile: A CSV File containing JSON information
        :type x: String

        :rtype: String
        '''
        # Create a ditionary
        resultDict = {}
        # Time complexity O(|N|) = O(|Number of rows|)
        with open(csvFile, 'r') as csvFile:
            reader = csv.reader(csvFile)
            # Skip first line containing column information
            next(reader) 
            for line in reader:
                country_id = line[2]
                if country_id == "BDV":
                    siteID = line[3]
                    userID = line[1]
                    # If siteID already is a key in dictionary
                    if resultDict.get(siteID) != None:
                        # if userID is unique append
                        if userID not in resultDict.get(siteID):
                            resultDict[siteID].append(userID)
                    else:
                        #  If key doesn't exist initialize a list with userID
                        resultDict[siteID] = [userID]
        maximum = 0
        mostUniqueUsers = ""
        # Find maximum and print result
        for item in resultDict:
            # print("%s: %d Unique Users" % (item,len(resultDict.get(item))))
            if len(resultDict.get(item)) > maximum:
                maximum = len(resultDict.get(item))
                mostUniqueUsers = item

        return (mostUniqueUsers, maximum)

    def moreThanTenTimes(self, csvFile):
        '''
        Between 2019-02-03 00:00:00 and 2019-02-04 23:59:59, there are four users who 
        visited a certain site more than 10 times. Find these four users & which sites 
        they (each) visited more than 10 times. (Simply provides four triples in the form 
        (userID, siteID, number of visits) in the box below.)

        :param csvFile: A CSV File containing JSON information
        :type x: String

        :rtype: None
        '''
        # Create a ditionary
        siteDict = {}
        uniqueDict = {}

        # Time complexity O(|N|) = O(|Number of rows|)
        with open(csvFile, 'r') as csvFile:
            reader = csv.reader(csvFile)
            # Skip first line containing column information
            next(reader) 
            for line in reader:
                ts = line[0]

                if ts > '2019-02-02 23:59:59' and ts < '2019-02-05 00:00:00':
                    siteID = line[3]
                    userID = line[1]
                    # Dictionary of all user interaction
                    if siteDict.get(siteID) != None:
                        siteDict[siteID].append(userID)
                    else:
                        siteDict[siteID] = [userID]

                    # Dictionary of unique user to iterate later
                    if uniqueDict.get(siteID) != None:
                        if userID not in uniqueDict.get(siteID):
                            uniqueDict[siteID].append(userID)
                    else:
                        uniqueDict[siteID] = [userID]
            
        result = []
        for item in uniqueDict:
            if len(siteDict.get(item)) > 10:
                for i in xrange(len(uniqueDict.get(item))):
                    # Use count function to count the number of occurance of the current item
                    numVisited = siteDict.get(item).count(uniqueDict.get(item)[i])
                    # If visited more than 10 times, print the desired results
                    if numVisited > 10:
                        # print("User %s visited Site: %s   %d times" % (siteDict.get(item)[i],item, numVisited))
                        result.append((siteDict.get(item)[i],item, numVisited))
                        # print("(%s, %s, %d)" % (siteDict.get(item)[i],item, numVisited))
        return result


    def topLastVisited(self, csvFile):
        '''
        For each site, compute the unique number of users whose last visit (found in the original data set) was 
        to that site. For instance, user "LC3561"'s last visit is to "N0OTG" based on timestamp data. 
        Based on this measure, what are top three sites? (hint: site "3POLC" is ranked at 5th with 
        28 users whose last visit in the data set was to 3POLC; simply provide three pairs 
        in the form (siteID, number of users).)

        :param csvFile: A CSV File containing JSON information
        :type x: String

        :rtype: List of Tuples
        '''
        # Create a ditionary
        tsDict = {}

        # Time complexity O(|N|) = O(|Number of rows|)
        with open(csvFile, 'r') as csvFile:
            reader = csv.reader(csvFile)
            # Skip first line containing column information
            next(reader) 
            for line in reader:
                newTimeStamp = line[0]
                userID = line[1]
                siteID = line[3]
                
                if tsDict.get(userID) != None:
                    # Get current timestamp and new timestamp
                    currTimeStamp = tsDict.get(userID)[0][0]
                    # If current timestamp is earlier than new timestamp
                    if currTimeStamp < newTimeStamp:
                        # Update the dictionary
                        tsDict[userID] = [[newTimeStamp,siteID]]  
                else:
                    tsDict[userID] = [[newTimeStamp, siteID]]

        # In final dictionary store the number of times visited
        # {'RT9Z6': 2, 'N0OTG': 561, '5NPAU': 992, 'JSUUP': 1, 'EUZ/Q': 1, 'GVOFK': 42, '3POLC': 28, 'QGO3G': 289}        
        finalDict = {}
        for item in tsDict:
            siteID = tsDict.get(item)[0][1]
            if finalDict.get(siteID) != None:
                finalDict[siteID] += 1
            else:
                finalDict[siteID] = 1

        # Sort the final Dictionary
        temp = {}
        # Make sure you write reverse=True
        temp = sorted(finalDict.iteritems(), lambda x, y : cmp(x[1], y[1]), reverse=True)
        
        # Return the first 3 elements of the sorted dictionary
        return (temp[0], temp[1], temp[2])


    def firstAndLastVisited(self, csvFile):
        '''
        For each user, determine the first site he/she visited and the last site he/she visited based on the timestamp data. 
        Compute the number of users whose first/last visits are to the same website. What is the number?

        :param csvFile: A CSV File containing JSON information
        :type x: String

        :rtype: Integer
        '''
        # Create a ditionary
        firstTsDict = {}
        lastTsDict = {}

        # Time complexity O(|N|) = O(|Number of rows|)
        with open(csvFile, 'r') as csvFile:
            reader = csv.reader(csvFile)
            # Skip first line containing column information
            next(reader) 
            for line in reader:
                # Get the new timestamp to compare
                newTimeStamp = line[0]
                userID = line[1]
                siteID = line[3]
                
                if firstTsDict.get(userID) != None:
                    # Get current timestamp and new timestamp
                    currTimeStamp = str(firstTsDict.get(userID)[0][0])
                    # If current timestamp is later than new timestamp
                    if currTimeStamp > newTimeStamp:
                        # Update the dictionary
                        firstTsDict[userID] = [[newTimeStamp,siteID]]  
                else:
                    firstTsDict[userID] = [[newTimeStamp, siteID]]
                
                if lastTsDict.get(userID) != None:
                    # Get current timestamp and new timestamp
                    currTimeStamp = str(lastTsDict.get(userID)[0][0])
                    # If current timestamp is earlier than new timestamp
                    if currTimeStamp < newTimeStamp:
                        # Update the dictionary
                        lastTsDict[userID] = [[newTimeStamp,siteID]]  
                else:
                    lastTsDict[userID] = [[newTimeStamp, siteID]]

        count = 0
        for item in firstTsDict:
            firstSiteID = firstTsDict.get(item)[0][1]
            lastSiteID = lastTsDict.get(item)[0][1]
            # if the siteID matched, increment the counter
            if firstSiteID == lastSiteID:
                count += 1
        
        return count


        
        

if __name__ == "__main__":
    solution = Solution()
    # lst = [{"userID" : "uid_1", "product_id" : "pid_1", "quantity" : 45}, {"userID" : "uid_1", "product_id" : "pid_2", "quantity" : 1}, {"userID" : "uid_2", "product_id" : "pid_2", "quantity" : 5}]
    
    # ================== Solution Q3 (A) ========================================================================
    print(solution.mostUniqueUsers('q3Data.csv'))           # Answer = ('5NPAU', 544)
    # There are total 544 + 2 + 90 = 636 Unique Users
    # Output : 5NPAU: 544 Unique Users
    # 3POLC: 2 Unique Users
    # N0OTG: 90 Unique Users
    # 5NPAU
    # Answer = 5NPAU

    # ================== Solution Q3 (B) ========================================================================
    print(solution.moreThanTenTimes('q3Data.csv'))          # Answer = [('LC376D', 'N0OTG', 26), ('LC376D', 'N0OTG', 25), ('LCC377', 'N0OTG', 17), ('LC3C7E', '3POLC', 15)]
    # Output :
    # (LC376D, N0OTG, 26)
    # (LC376D, N0OTG, 25)
    # (LCC377, N0OTG, 17)
    # (LC3C7E, 3POLC, 15)
    # OR
    # User LC376D visited Site: N0OTG   26 times
    # User LC376D visited Site: N0OTG   25 times
    # User LCC377 visited Site: N0OTG   17 times
    # User LC3C7E visited Site: 3POLC   15 times

    # ================== Solution Q3 (C) ========================================================================
    print(solution.topLastVisited('q3Data.csv'))            # Answer = (('5NPAU', 992), ('N0OTG', 561), ('QGO3G', 289))
    # Output :
    # (('5NPAU', 985), ('N0OTG', 561), ('QGO3G', 293))

    # ================== Solution Q3 (D) ========================================================================
    print(solution.firstAndLastVisited('q3Data.csv'))       # Answer = 1670





    

