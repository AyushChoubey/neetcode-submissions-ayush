class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        bounds = set()

        for r in range(len(board)):
            for c in range(len(board[0])):

                if r ==0 or r == len(board)-1 or c ==0 or c == len(board[0])-1:
                    if board[r][c] =="O" :
                        bounds.add((r,c))

                    
        def dfs(box,board):
            if box in visited:
                return 
            visited.add(box)

            r,c = box
            board[r][c] = '#'

            for d in dirs:
                next_r = r+d[0]
                next_c = c+d[1]
                box = (next_r,next_c)
                
                if box not in visited:

                    if self.is_within_bounds(next_r,next_c,board) and board[next_r][next_c] == "O" :
                        
                        dfs(box,board)

        

            

        for box in bounds:
            if box not in visited:

               dfs(box,board)

        # print(board)
        for r in range(len(board)):
            for c in range(len(board[0])):

                
                if board[r][c] =="O" :
                    board[r][c] ="X"

                if board[r][c] =="#" :
                    board[r][c] ="O"
                    



    def is_within_bounds(self, r,c,heights):
         return 0<=r<len(heights) and 0<= c< len(heights[0])
                  

        
        