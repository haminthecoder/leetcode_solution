class Solution():
    def coinChange(self, coins, amount):
        # input coin => List output => integer
        # 
        # [1,2,5] => 11
        # 1 * 11 [0,1,2,3,4,5,...,11]
        # 5,5,1 [0,...,1,,,,2,3] min(11, 3) = 3 
        # dp = [0] + [float("inf")] * amount
        # for loop coins iterate => 1 -> amount + 1
        #   for coin in coins:
        #       i - coin >= 0
        #       dp[i] = min(dp[i], dp[i-coin] + 1)
        
        dp = [0] + [float("inf")] * amount
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]

test = Solution()
print(test.coinChange([2,3,7,10], 150))
        