# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)

        visit = set()
        path = set()

        def dfs(course: int) -> bool:
            if course in visit:
                return True
            if course in path:
                return False

            path.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            path.remove(course)

            visit.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
