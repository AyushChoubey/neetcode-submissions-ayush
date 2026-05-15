class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        edge_tracker = {}
        # graph = {}
        # def make_graph(prerequisites,graph):
        #     for edge in prerequisites:
        #         if edge[0] not in graph:
        #             graph[edge[0]] = []
        #         if edge[1] not in graph:
        #             graph[edge[1]] = []
                
        #         graph[edge[0]].append(edge[1])
        #     return graph 

        graph = {i:[] for i in range(numCourses)}

        for course ,prereq in prerequisites:
            graph[course].append(prereq)
        
        
            
        self.path = []
        def dfs(node,path_visited):
            
            if node in path_visited :
                # print('yay')
                nonlocal cycle_detected
                # print(node,visited,'----')
                cycle_detected = True
                return 
            if node in global_visited:
                # print(global_visited)
                return 

            
            
            path_visited.add(node)
           
            
                
            #print(node,path_visited,global_visited)
            print(node)
            
            for n in graph[node]:
               
                dfs(n,path_visited)
            path_visited.remove(node)
            global_visited.add(node)
            self.path.append(node)

            

            
        result =[]
        # make_graph(prerequisites,graph)
        # print(graph)
        cycle_detected = False
        global_visited = set()
        for node in graph:
            
            path_visited = set()
            # track = set()
            if node not in global_visited:
                dfs(node,path_visited)
        # print(cycle_detected)
        
        if  not cycle_detected :
            return self.path
        else:
            return []
        