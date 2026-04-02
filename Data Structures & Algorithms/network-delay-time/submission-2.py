class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list  = {}
        for  i in times:
             if i[0] not in adj_list:
                adj_list[i[0]] = []
             adj_list[i[0]].append((i[1],i[2]))

        # print(adj_list)

        min_heap = []
        heapq.heappush(min_heap,(0,k))
        visited = [0]*n
        min_dist = [float('inf')]*n

        node_dist= 0
        while min_heap != []:
            # print(min_dist) 
            
            dist,node = heapq.heappop(min_heap)
            if visited[node-1] == 0:
                visited[node-1] = 1
                # print(node, node_dist, dist,min_dist[node-1] )
                if  dist< min_dist[node-1]:
                    min_dist[node-1] = dist
                if node in adj_list.keys():
                    for i in adj_list[node]:
                        parent_node_dist = min_dist[node-1]
                        heapq.heappush(min_heap,(i[1]+min_dist[node-1],i[0]))
            
        # print(min_dist)  















        

        


        if max(min_dist) == float('inf'):
            return -1
        else:
            return max(min_dist)
        