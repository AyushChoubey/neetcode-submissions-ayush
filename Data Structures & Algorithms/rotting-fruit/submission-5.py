from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def make_graph(grid):
            graph = {}
            indexes = [(0,1),(0,-1),(1,0),(-1,0)]
            s = []
            rows, cols = len(grid), len(grid[0])

            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1 or grid[row][col] == 2:
                        node = row * cols + col
                        if node not in graph:
                            graph[node] = []
                        for i in indexes:
                            nr, nc = row + i[0], col + i[1]
                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == 1 or grid[nr][nc] == 2:
                                    graph[node].append(nr * cols + nc)
                        if grid[row][col] == 2:
                            s.append(node)

            return graph, s

        def bfs(graph, s, visited, cnt):
            q = deque(s)
            for node in s:
                visited.add(node)

            while q:
                new_added = False
                l = len(q)
                for _ in range(l):
                    node = q.popleft()
                    for n in graph[node]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
                            new_added = True
                if new_added:
                    cnt += 1

            return cnt, visited

        # check fresh oranges
        fresh = sum(grid[r][c] == 1
                    for r in range(len(grid))
                    for c in range(len(grid[0])))
        if fresh == 0:
            return 0

        graph, s = make_graph(grid)

        if not s:
            return -1

        cnt, visited = bfs(graph, s, set(), 0)

        if len(visited) != len(graph):
            return -1
        return cnt