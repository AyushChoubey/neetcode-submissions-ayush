class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_dict = {}

        for  row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] ==".":
                    continue
                block = 3*(row//3)+col//3

                if board[row][col] not in num_dict:
                    num_dict[board[row][col]] =[[row,col,block]] 
                else:
                    for i in num_dict[board[row][col]]:
                        if i[0]==row or i[1] ==col or i[2] ==block:
                            print(i[0],row,i[1],col, i[2],block,board[row][col])
                            return False
                    
                    num_dict[board[row][col]].append([row,col,block])

        return True 
        