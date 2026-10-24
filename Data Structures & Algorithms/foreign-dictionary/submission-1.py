from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        nodes = {c: set() for word in words for c in word}

        i = 0 

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    nodes[w1[j]].add(w2[j])
                    break
            
        
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = False
            
            for neighbor in nodes[char]:
                if not dfs(neighbor):
                    return False
                
            visited[char] = True
            res.append(char)
            return True
        
        for char in nodes:
            if not dfs(char):
                return ""
        
        return "".join(res[::-1])
            
                
                

        