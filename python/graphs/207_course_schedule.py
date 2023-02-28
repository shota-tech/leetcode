# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre_courses = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_courses[course].append(pre)

        visit = set()

        def dfs(course: int) -> bool:
            if course in visit:
                return False

            if not pre_courses[course]:
                return True

            visit.add(course)
            for pre in pre_courses[course]:
                if not dfs(pre):
                    return False

            visit.remove(course)
            pre_courses[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
