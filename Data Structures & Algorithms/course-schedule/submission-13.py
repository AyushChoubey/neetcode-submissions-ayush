class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # I think we just have to find the cycle beasue if we have a cylce then there is no way you can complete the courses

        #  how to detect a cycle we need to check for every dfs run if it visits the same node again then there is a cycle
        # we need to update the visited at every dfs run because same node can be visted if it has two dependencies but they are not connected 
        # maybe two visited one to check overall run and one for that particular run let's try 
        # or we can track edges instead of nodes that will make differnce as we we go to same edge again there is  a cycle else 
        # not, let's track edges :
        # But,
        # I thought to detect a cycle i just have to check if a node is visited for a particular dfs run from a node but it failed for example like this
        # [[1,4],[2,4],[3,1],[3,2]] because dfs run from 3 reaches 4 two times even if its not a cycle. which made me think i must forget the
        # visited if i get returned from one path so we need to maintain  a path wise visited  

        
        edge_tracker = {}
        graph = {}
        def make_graph(prerequisites,graph):
            for edge in prerequisites:
                if edge[0] not in graph:
                    graph[edge[0]] = []
                if edge[1] not in graph:
                    graph[edge[1]] = []
                
                graph[edge[0]].append(edge[1])
            return graph 
        
        
            

        def dfs(node,path_visited):
            
            if node in path_visited :
                # print('yay')
                nonlocal cycle_detected
                # print(node,visited,'----')
                cycle_detected = True
                return 
            if node in global_visited:
                return 

            
            
            path_visited.add(node)
            # print(node,visited)
            
            for n in graph[node]:
               
                dfs(n,path_visited)
            path_visited.remove(node)
            global_visited.add(node)

            

            
        result =[]
        make_graph(prerequisites,graph)
        # print(graph)
        cycle_detected = False
        for node in graph:
            global_visited = set()
            path_visited = set()
            if node not in global_visited:
                dfs(node,path_visited)
        # print(cycle_detected)
        return not cycle_detected 
        
            
            

        