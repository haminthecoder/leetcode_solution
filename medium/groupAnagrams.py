class Solution:
    # Dictionary
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in result:
                result[sortedWord] += [word]
            else:
                result[sortedWord] = [word]
        answer = []
        for item in result:
            answer.append(result[item])
                
        return answer
    #   return [ anas[x] for x in anas ]


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = strs.copy()
        answer = []
        d = {}
        
        for i in range(len(strs)):
            tmp = sorted(copy[i])
            copy[i] = "".join(tmp)
            
        for i in range(len(copy)):
            d[copy[i]] = d.get(copy[i], []) + [strs[i]]
                    
        for item in d.values():

            answer.append(item)
        
        return answer
        
    
                
            
                