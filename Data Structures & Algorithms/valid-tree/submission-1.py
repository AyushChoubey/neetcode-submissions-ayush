class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # return len(edges) == n-1 this wont work as graphs can have multiple connected components that leads to error 

        # lets calculate tota number of ccnums: If it's 1 then we use the above validation else we return flase as 
        # tree are always connected

        graph = {i:[] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

        visited= set()
        cc_num = 0
        for node in graph:
           if node not in visited:
                dfs(node)
                cc_num +=1

        if cc_num==1 :
            return len(edges) == n-1
        else:
            return False 


        