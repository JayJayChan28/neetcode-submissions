class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adj list
        #base case: no outgoing edges: meaning no more prerequreisites
        #use cycle set --> for cycle detections, topological sort

        adj_list = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj_list[course].append(pre)

        cycle = set()

        def dfs(course):
            #base case, no more courses
            if adj_list[course] == []:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for pre in adj_list[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            adj_list[course] = []
            return True
        
        for course in adj_list:
            if dfs(course) == False:
                return False
        return True
