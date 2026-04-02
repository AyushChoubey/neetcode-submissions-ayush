class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #so we need to send the length of largest connected components
        #copying make_graph from prev solution of number of islands
        def make_graph(grid):
            G = {}
            H_len = len(grid[0])
            V_len = len(grid)
            # print(V_len,H_len)
            for i in range(V_len):
                for j in range(H_len):
                    if grid[i][j] == 1:
                        G[ H_len*i+j]  = []
                        
                        if i-1 >=0 and grid[i-1][j] == 1:
                            G[H_len*i+j].append(H_len*(i-1)+j)
                            
                        if i+1 < V_len and grid[i+1][j] == 1:
                            G[H_len*i+j].append(H_len*(i+1)+j)
                            
                        if j-1 >=0  and grid[i][j-1] == 1:
                            G[H_len*i+j].append(H_len*(i)+(j-1))
                            
                        if j+1 <  H_len and grid[i][j+1] == 1:
                            G[H_len*i+j].append(H_len*(i)+(j+1))
            # print(G)               
            return G  

        def dfs(node,is_visited,G,lent):
            if is_visited[node]== True:
                # print(lent)
                return lent
            
            is_visited[node] = True
            # print(lent)
            for n in G[node]:
                
                if is_visited[n] == False:
                    
                   lent =  dfs(n,is_visited,G,lent+1)

            return lent

        


        G = make_graph(grid)

        is_visited = {}

        for i in G.keys():
            is_visited[i] = False
        cc_len = []
        cc_num = 0

        # print(G)
        for  node in G.keys():
            if is_visited[node] == False:
                
                lent  = dfs(node,is_visited,G,1)
                cc_num +=1
                cc_len.append(lent)
        # print(cc_num,cc_len)
        if (len(cc_len) >0):
            return max(cc_len)
        else:
            return 0 

