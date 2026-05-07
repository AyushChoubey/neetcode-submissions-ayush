class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        q = []
        for r in range(len(grid)):
                row = []
                for c in range(len(grid[0])):
                    if grid[r][c] == 0:
                        q.append((r,c))
                        
                
                    
        
        distance = 0   
        INF = 2147483647       

        while q:
            distance +=1
            for _ in range(len(q)):
                r,c = q.pop(0)
                


                for d in dirs:
                    next_r,next_c = r+d[0], c+d[1]
                    if  self.is_within_bounds( next_r,next_c,grid) and grid[next_r][next_c] == INF:

                        grid[next_r][next_c] = distance
                        q.append((next_r,next_c))
        
        


                    

        









    def is_within_bounds(self, r,c,grid):
        return 0<=r<len(grid) and 0<= c< len(grid[0])

            
                    
            
