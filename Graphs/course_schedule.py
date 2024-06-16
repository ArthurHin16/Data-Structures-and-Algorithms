def can_finish(num_courses, prerequisites):
    preMap = {i: [] for i in range(num_courses)}

    # map each course to : prereq list
    for course, prerequisite in prerequisites:
        preMap[course].append(prerequisite)
    print(preMap)
    visiting = set()

    # DFS
    def dfs(course):
        if course in visiting:
            return False
        if preMap[course] == []:
            return True
        visiting.add(course)
        for precourse in preMap[course]:
            if not dfs(precourse):
                return False
        visiting.remove(course)
        preMap[course] = []
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True


numCourses = 2
prerequisites = [[1,0]]
print(can_finish(numCourses, prerequisites))