from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        q = deque()
        min_dist = [float("inf")]*n
        min_dist[src] = 0

        q.append((src,0))
        graph  ={}
        for i in flights:
                if i[0] not in graph:
                    graph[i[0]] = []
                if i[1] not in graph:
                    graph[i[1]] = []
                graph[i[0]].append((i[1],i[2]))

        while q and k>=0:
            
            l= len(q)

            for _ in range(l):
                # print(q)
                node,dist = q.popleft()



                

                for n in graph[node]:
                    if min_dist[n[0]]> dist+n[1]:
                        min_dist[n[0]]  = dist+n[1]
                        q.append((n[0],min_dist[n[0]]))
            k-=1
        # print(min_dist)
        if min_dist[dst] != float('inf'):

            
            return min_dist[dst]
        else:
            return -1
