class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there is a cycle - you return false 
        nodes = set()
        adjList = {}
        def constructGraph(): 
            for course, prereq in prerequisites: 
                nodes.add(course)
                nodes.add(prereq)
                if prereq not in adjList: 
                    adjList[prereq] = []
                if course not in adjList: 
                    adjList[course] = []
                adjList[prereq].append(course)


        visited = set()
        def dfs(src): 
            if src in visited: 
                return False
            
            if len(adjList[src]) == 0: 
                return True 
            
            visited.add(src)
            for neighbor in adjList[src]: 
                if not dfs(neighbor): 
                    return False 

            visited.remove(src)
            adjList[src] = []
                
            return True
            
        constructGraph()

        for n in nodes: 
            val = dfs(n)
            if val == False:
                return False

        return True