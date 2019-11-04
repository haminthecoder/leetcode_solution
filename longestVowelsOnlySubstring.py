class Solution:
    def longestVowelsOnlySubstring(self, S):
        # Set is an unordered list that doesn't allow duplicate values
        # List is an ordered list that allows duplicate values
        vowels = set('aeiou')
        result = 0
        return result
    def divisible_by_7(self, lst):
        """Return True if and only if lst contains an element divisible
        by 7. Otherwise, return False.

        >>> divisible_by_7([4,8,21,6])
        True
        >>> divisible_by_7([1,2,8,9])
        False
        """
        for num in lst:
            if num % 7 == 0:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.divisible_by_7([4,8,21,6]))
    print(solution.divisible_by_7([1,2,8,9]))

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         '''
#         Empty - 0
#         Fresh orange - 1
#         Rotten - 2
        
#         adjacent to rotten orange =>  
#         '''
#         dictOrange = {}
#         flag1, flag2 = False, False
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == 2:
#                     flag1 = True
#                 if grid[i][j] == 1:
#                     flag2 = True
#                 dictOrange[i*3 + j] = grid[i][j]
#         if flag1 == True and flag2 == False:
#             return 0
        
#         noFreshNear = True
#         counter = 0
#         for i in range(len(dictOrange)):
#             if dictOrange[i] == 2:
#                 tmp = False
#                 if i + 3 < len(dictOrange):
#                     if dictOrange[i+3] == 1:
#                         dictOrange[i+3] = 2
#                         tmp = True
#                         noFreshNear = False
#                 if i - 3 > -1:
#                     if dictOrange[i-3] == 1:
#                         dictOrange[i-3] = 2
#                         tmp = True
#                         noFreshNear = False
#                 if i + 1 < len(dictOrange) and (i+1) % 3 != 0:
#                     if dictOrange[i+1] == 1:
#                         dictOrange[i+1] = 2
#                         tmp = True
#                         noFreshNear = False
#                 if i - 1 > -1 and (i-1) % 3 != 1:
#                     if dictOrange[i-1] == 1:
#                         dictOrange[i-1] = 2
#                         tmp = True
#                         noFreshNear = False
#                 if tmp == True:
#                     counter += 1
            
#         for i in range(len(dictOrange)):
#             if dictOrange[i] == 1:
#                 return -1
        

#         return counter
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         '''
#         Given a positive integer n, generate a square matrix 
#         filled with elements from 1 to n2 in spiral order.

#         '''
        