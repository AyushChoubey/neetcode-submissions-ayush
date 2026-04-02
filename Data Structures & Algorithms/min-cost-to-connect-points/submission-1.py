class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def make_graph(points):
            graph = {}
            # for  i in range(len(points)):
            #     for j in range(i+1, len(points)):
            #         if tuple(points[i]) not in graph.keys():
            #             graph[tuple(points[i])] = []
            #             graph[tuple(points[i])].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),tuple(points[j])))
            #         else:
            #             graph[tuple(points[i])].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),tuple(points[j])))
            #         if tuple(points[j]) not in graph.keys():
            #             graph[tuple(points[j])] = []
            #             graph[tuple(points[j])].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),tuple(points[i])))
            #         else:
            #             graph[tuple(points[j])].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),tuple(points[i])))
            for  i in range(len(points)):
                for j in range(i+1, len(points)):
                    if  i not in graph.keys():
                        graph[i] = []
                        graph[i].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),j))
                    else:
                        graph[i].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),j))
                    if j not in graph.keys():
                        graph[j] = []
                        graph[j].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i))
                    else:
                        graph[j].append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]),i))
            return graph

        graph = make_graph(points)
        inMST =[0]*len(points)
        dist = [float("inf")]*len(points)
        # print(graph)


        min_heap = []
        heapq.heappush(min_heap,(0,0))

        while min_heap!=[]:
            min_dist, node = heapq.heappop(min_heap)
            
            if inMST[node] == 0:
                inMST[node] = 1
                if  min_dist< dist[node]:
                    dist[node] = min_dist
                if node in graph.keys():
                    for i in graph[node]:
                        heapq.heappush(min_heap,(i[0],i[1]))


        # def MST(graph)

        return sum(dist)