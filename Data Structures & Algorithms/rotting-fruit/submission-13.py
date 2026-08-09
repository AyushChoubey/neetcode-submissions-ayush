from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        src = (-1,-1)
        ones = 0
        q = deque([])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:

                    
                    src = (row,col)
                    q.append(src)
                    
                    # count+=1
                    
                if grid[row][col] == 1:
                    ones+=1

       

       
        mnts = 0
        visited = set()
        while q and ones>0:

            l = len(q)
            print("l",l,q)
            for i in range(l):

                row,col = q.popleft()
                print(row,col,count)
                
                # print(row,col,count)



                for d in dirs:

                    new_col = d[0]+row
                    new_row =  d[1]+col

                    if self.check_bound(new_row,new_col,grid) and grid[new_row][new_col] == 1 and (new_row,new_col) not in visited:
                        ones-=1
                        q.append((new_row,new_col))
                        visited.add((new_row,new_col))
            mnts+=1
        # print(count,mnts)
        return mnts if ones== 0 else -1

    def check_bound(self,row,col,grid):
        return 0<=row<len(grid) and 0<= col <len(grid[0])
         


        
        