class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {course : [] for course in range(numCourses)}

        for i, j in prerequisites:
            preMap[i].append(j)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                return True
            
            visit.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visit.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

