class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #create adj list
        adj_list = {i: [] for i in range(numCourses)}

        #adj list finished
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        print(adj_list)
        cycle = set()
        visited = set()
        res = []

        def dfs(course):
            #if we detect a cycle within the sam DFS call
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)            
            for pre in adj_list[course]:

                #IMPORATNT we need this so that when we detect a cycle we dont recursivelyt go even deeper, we need to immediialy stop
                if not dfs(pre):
                    return False

            #backtracking step, we finsihed this dfscall lets explore other paths
            cycle.remove(course)

            #Also need to add cisited 
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return res

                