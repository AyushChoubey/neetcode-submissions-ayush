class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = {}
        result =[]

        for src,dst in sorted(tickets):
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)

        

        def dfs(node):
            while(graph.get(node)):
                next_node = graph[node].pop(0)

                dfs(next_node)
            result.append(node)
        dfs('JFK')

        return result[::-1]
        