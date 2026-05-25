import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        # I guess fidn the maximum in the shortest path will work


        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        


        min_heap = []
        heapq.heappush(min_heap,(grid[0][0],(0,0)))
        path = []
        last_node = (len(grid)-1)* (len(grid[0])-1)
        # dist = {node:float("-inf") for i in range(last_node) }
        dist = {}
        prev = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dist[(i,j)] = float("inf")
                prev[(i,j)] = None

        dist[(0,0)] = grid[0][0]
        # print(prev,dist)




        # priv = {node:None for i in range(last_node) }
        while min_heap:
            d,cords = heapq.heappop(min_heap)
            r,c = cords[0], cords[1]
            # node = r*(len(grid[0])-1)+c
            # print(min_heap)
            if dist[(r,c)]<d:
                continue

            for d in dirs:
                next_r = d[0]+r
                next_c = d[1]+c
                # next_node = next_r*(len(grid[0])-1)+next_c
                if self.check_bounds(grid,next_r,next_c):

                    new_dist = dist[(r,c)]+grid[next_r][next_c] - grid[r][c] # <--this is so important part which is substracting the current node value becuase by the time you reach the node all the nodes smaller or equal to that node could swim directly to the those nodes no need to wait so we subtract the current node value   
                    # print(new_dist,dist[(r,c)])

                    if new_dist<dist[(next_r,next_c)]:
                       
                        dist[(next_r,next_c)] = new_dist
                        prev[(next_r,next_c)] = (r,c)
                        heapq.heappush(min_heap,(new_dist,(next_r,next_c)))
        # print(prev)
        max_val,path = self.get_path(grid,prev,(0,0),(len(grid)-1,len(grid[0])-1))
        # print(path)
        return max_val





        




    def get_path(self,grid,prev, source, target):
        path = []
        current = target
        # value = []
        max_val = float("-inf")

        while current is not None:
            path.append(current)
            # print(current[0],current[1])
            if grid[current[0]][current[1]]> max_val:
                max_val = grid[current[0]][current[1]]
            
            current = prev[current]   # ← follow predecessors backward

        # path.reverse()                # ← reverse to get source→target order

        # if path[0] == source:
        # print(path)
        return max_val,path
        # return []   # no path exists
    


    def check_bounds(self,grid,r,c):
        return (0<=r<=len(grid)-1) and (0<=c<=len(grid[0])-1)
