#solution: approach 1
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = {}

        if strs == "":
            return [[""]]
        else:
            for st in strs:
                key = ",".join(sorted(st))
                if key not in hash :
                    hash[key] = [st]
                else:   
                    hash[key].append(st)

            result = list(hash.values())
            return result

"""
#solution: approach 2

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = defaultdict(list)
        for st in strs:
            
            count = [0]*26

            for char in st:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)

            hash[key].append(st)

        
        return list(hash.values())