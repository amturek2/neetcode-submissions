class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a valid tree is acyclic 
        # start at one end if there are disconnected components or cycles we will
        # return 
        from collections import deque
        from collections import defaultdict
                

        nodes = set()
        adjList = defaultdict(list)

        for s,t in edges: 
            adjList[s].append(t)
            adjList[t].append(s)
            nodes.add(s)
            nodes.add(t)

        visited = set()

        def bfs(src): 
            q = deque()
            q.append((None, src))
            visited.add(src)

            while q: 
                parent, curr = q.popleft()
                print(parent, curr)
                for neighbor in adjList[curr]: 
                    if neighbor == parent:
                        continue 
                    if neighbor not in visited: 
                        q.append((curr, neighbor))
                        visited.add(neighbor)
                    else: 
                        return False
            return True


        if not bfs(0):
            return False

        if len(visited) < n: 
            return False
        
        return True
    
