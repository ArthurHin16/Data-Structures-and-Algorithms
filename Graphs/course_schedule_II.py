def course_schedule_II(numCourses, prerequistes):
    prereq = {c: [] for c in range(numCourses)}

    for course, pre in prerequisites:
        prereq[course].append(pre)

    output = []
    visit, cycle = set(), set()

    def dfs(course):
        if course in cycle:
            return False
        if course in visit:
            return True
        cycle.add(course)
        for pre in prereq[course]:
            if dfs(pre) == False:
                return False
        cycle.remove(course)
        visit.add(course)
        output.append(course)
        return True
    
    for course in range(numCourses):
        if dfs(course) == False:
            return []
        
    return output

numCourses = 2
prerequisites = [[1,0]]
print(course_schedule_II(numCourses, prerequisites))
