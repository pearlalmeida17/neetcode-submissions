class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        res = []

        visit = [0] * numCourses

        def dfs(course):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True

            visit[course] = 1

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visit[course] = 2
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
                

            


            

