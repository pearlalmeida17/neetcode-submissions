from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        all_combos = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j +1 :]
                all_combos[pattern].append(word)
            
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, level = queue.popleft()

            if current_word == endWord:
                return level

            for j in range(len(current_word)):
                pattern = current_word[:j] + "*" + current_word[j +1 :]
                
                for neighbor in all_combos[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append([neighbor, level + 1])
                        
                all_combos[pattern] = []

            
        return 0 


            
