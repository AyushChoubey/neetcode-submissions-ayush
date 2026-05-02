class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        q = []
        ones ,seconds = 0,0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] ==1:
                    ones +=1
                elif grid[r][c] ==2:
                    q.append((r,c))
        while q and ones>0:
            seconds+=1
            for _ in range(len(q)):
                r,c = q.pop(0)
                for d in dirs:
                    next_r,next_c = r+d[0],c+d[1]
                    if self.is_within_bounds(next_r,next_c,grid) and grid[next_r][next_c] ==1:
                        q.append((next_r,next_c))
                        ones-=1
                        grid[next_r][next_c] =2
        return seconds if ones==0 else -1

    def is_within_bounds(self, r,c,grid):
        return 0<=r<len(grid) and 0<= c< len(grid[0])




