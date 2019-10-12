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

    # Brute Force
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     result = []
    #     for i in range(len(strs)):
    #         if not result:
    #             result.append([strs[i]])
    #             other.append(sorted(strs[i]))
    #         else:
    #             flag = False
    #             for j in range(len(result)):
    #                 tmp = sorted(result[j][0])
    #                 if tmp == sorted(strs[i]):
    #                     result[j].append(strs[i])
    #                     flag = True
    #                     break
    #             if flag == False:
    #                 result.append([strs[i]])
    #     return result
    
                
            
                