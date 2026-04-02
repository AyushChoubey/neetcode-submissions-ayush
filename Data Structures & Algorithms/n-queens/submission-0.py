class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.result = []
        row_list = ['.' for i in range (n)]
        def get_n_queen(n,start_row,path,row_list):
            if len(path)== n:
                self.result.append(path.copy())
                return
            # print(path)
            # for row in range(start_row,n):
            for col in range(n):
                dig_check = True
                col_check = True
                for p in range(len(path)-1,-1,-1):
                    idx = path[p].index('Q')
                    if idx == col:
                        col_check =False
                    if idx == col+len(path)-p or idx == col-(len(path)-p) :
                        dig_check = False

                    

                if path !=[]:
                    
                    if dig_check and col_check:
                        new_row = row_list.copy()
                        new_row[col] = 'Q'
                        path.append(new_row)

                        get_n_queen(n,start_row+1,path,row_list)
                        path.pop()
                else:
                        new_row = row_list.copy()
                        new_row[col] = 'Q'
                        path.append(new_row)

                        get_n_queen(n,start_row+1,path,row_list)
                        path.pop()

        get_n_queen(n,0,[],row_list) 
        for i,j in  enumerate(self.result):
            for k,l in enumerate(j):
                self.result[i][k] = ''.join(l)     
        print(self.result)
        return self.result 
        