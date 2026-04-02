class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False
        def search(board,start_node,path):
            row = start_node[0]
            col = start_node[1]
            if len(path['word'])== len(word) or row ==len(board) or col==len(board[0]) or row==-1 or col == -1:
                # print(path)
                if ''.join(path['word']) == word:
                    self.result =True
                    return True 
                else:
                    return False
            # print(path)
            # print(row,col)
            positions = [[row+1,col],[row,col+1],[row-1,col],[row,col-1]]
            # print(row,col,positions)
            # print(path, positions)
            # print( len(board),len(board[0]),'---')
            
            for p in positions:
                
                if p not in path['cord'] and p[0]>=0 and p[1]>=0 and p[0] <len(board) and p[1]<len(board[0]) and len(path['word'])<= len(word):
                    path['word'].append(board[p[0]][p[1]])
                    path['cord'].append([p[0],p[1]])
                    # print(p,path)
                    search(board,p,path)
                    path['cord'].pop()
                    path['word'].pop()

            

        for row in range(len(board)):
            for col in range(len(board[row])):

                if board[row][col] == word[0] and self.result == False:
                    search(board,[row,col],{'word' : [word[0]],'cord':[[row,col]]})
        # print(self.result)
        return self.result