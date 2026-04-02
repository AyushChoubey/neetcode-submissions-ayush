class Solution:
    def make_graph(self,grid):
        G = {}
        H_len = len(grid[0])
        V_len = len(grid)
        # print(V_len,H_len)
        for i in range(V_len):
            for j in range(H_len):
                if grid[i][j] == "1":
                    G[ H_len*i+j]  = []
                    
                    if i-1 >=0 and grid[i-1][j] == "1":
                        G[H_len*i+j].append(H_len*(i-1)+j)
                        # print('^',G[H_len*i+j],H_len*(i-1)+j,'\n')
                    if i+1 < V_len and grid[i+1][j] == "1":
                        G[H_len*i+j].append(H_len*(i+1)+j)
                        # print('V', G[H_len*i+j],H_len*(i+1)+j,'\n')
                    if j-1 >=0  and grid[i][j-1] == "1":
                        G[H_len*i+j].append(H_len*(i)+(j-1))
                        # print('<',G[H_len*i+j],H_len*(i)+(j-1),'\n')
                    if j+1 <  H_len and grid[i][j+1] == "1":
                        G[H_len*i+j].append(H_len*(i)+(j+1))
                        # print('>',G[H_len*i+j],H_len*(i)+(j+1),'\n')
        return G 
    def dfs(self,G,is_visited,node):
        if is_visited[node] == True:
            return
        
        is_visited[node] = True
        print(is_visited)
        print(node)
        for n in G[node]:
            print(node,'->',n)
            if is_visited[n] == False:
                self.dfs(G,is_visited,n)

        # self.cc_num  +=1 THis is wrong, as it seems that this will only
        # increment in the fisrt call dfs(1) and never again as we will check 
        # that it is visited or not, and since all the nodes are visited in the 
        # fisrt call itself in the recursion.But it will reach here when the list of
        # edges ends for every node (for loop ends)
        
    

    def numIslands(self, grid: List[List[str]]) -> int:
        # seems like connected components problem

        #make graph by going to each element and if the current is 
        # 1 and left right up and down is a one make an edge between 
        # those, and in the end run connected componnent number on the built 
        #grpah 

        G = self.make_graph(grid)
        is_visited  = {}
        print(G)
        for k in G.keys():
            is_visited[k] = False
        self.cc_num = 0
        #Now run DFS
        for node in G.keys():
            if not is_visited[node]:
                self.dfs(G,is_visited,node)
                self.cc_num+=1
        print(self.cc_num)
        return self.cc_num

     