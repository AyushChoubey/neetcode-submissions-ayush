class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
       
        parent = list(range(len(edges)+1))

        def union(a,b):

            p1 = find(a)
            p2 = find(b)

            if p1 == p2:
                return False    # cycle!
            parent[p2] = p1
            return True

        def find(a):
            if parent[a] != a:
                

                parent[a] = find(parent[a])
            return parent[a]

            return parent[a]

        for a, b in edges:
            if not union(a, b):
                return [a, b]



