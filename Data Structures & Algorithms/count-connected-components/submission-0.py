class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        return cc_num


        