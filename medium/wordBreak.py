class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s = "skelterlabs" w = ["skel", 'terlabs', 'labs']
        # s= "sojung" w= ['so', 'jun']
        # stack = list(s)
        # index = set()
        # stack.pop(0)
        # currentWord = ""
        # while stack:
        # currentWord += stack.pop(0)
        # if currentWord in w:
        # currentWord = ""
        # index.add(wordDict.index(w))
        # return len(stack) == len(w)
                
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        currWord = ""
        
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i: j+1] in wordDict:
                        dp[j+1] = True
        return dp[-1]
        
        
                
        
        