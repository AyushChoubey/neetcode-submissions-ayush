class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = {}
        freq = {}
        
        for i,j in tickets:
            if i not in graph:
                graph[i] = []
                # freq[i] = 0
            if j not in graph:
                graph[j] = []
            if j not in freq:
                freq[j] = 0
            if i not in freq:
                freq[i] = 0
            
            freq[j]+=1
            
            graph[i].append(j)
        freq['JFK']+=1
        for node in graph:
            graph[node].sort() 
        print(graph)
        
        self.result = []
        self.track_edges = set((i,j) for i,j in tickets)

        def dfs(node):
            if freq[node] ==0:
                return
            
            freq[node]-=1
            #self.result.append(node)
            
            for n in graph[node]:

                if [node,n] in tickets:
                    tickets.remove([node,n])
                    
                    dfs(n)
            self.result.append(node)
            
            
            
        
         
        
        dfs('JFK')

        
        # print(self.track_edges,'yaya')


        return self.result[::-1]

        

            


        