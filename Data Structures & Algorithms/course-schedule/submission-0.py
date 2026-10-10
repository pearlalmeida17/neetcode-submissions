class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        path = set()

        def dfs(course):

            if course in path:
                return False
            if  preMap[course] == []:
                return True
            
            path.add(course)

            for pre in  preMap[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            preMap[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
    
                

                



