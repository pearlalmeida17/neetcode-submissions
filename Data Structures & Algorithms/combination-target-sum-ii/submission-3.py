class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subset = []

        def backtrack(index, current_sum):

            if current_sum == target:   
                res.append(subset.copy())
                return 

            if index == len(candidates) or current_sum >= target:
                return 
            
           
            subset.append(candidates[index])
            backtrack(index + 1, current_sum + candidates[index])

            subset.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            backtrack(index + 1, current_sum )
            
        backtrack(0, 0)
        return res


                
        