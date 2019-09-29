# Python version 3
class Solution:
    # Worst case time complexity O(N)
    # Space complexity O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = 0
        shortest_str = ""

        if not strs:
            return ""
        
        shortest_str = min(strs,key=len)

        # When finding shortest str via this method I got an 
        # Index out of range error

        # for word in strs:
        #     if shortest == 0 or shortest > len(word):
        #         shortest = len(word)
        #         shortest_str = word

        # Time complexity of enumerate
        # Initialization: O(1)
        # Returning the next element: O(1)
        # So in this case O(1)
        for i, char in enumerate(shortest_str):
        # Worst case O(N) runtime
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]
        
        return shortest_str
        