class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.result = []
        candidates.sort()
        def dfs(i,curr_sum,path):
            if curr_sum >= target  or i == len(candidates):
                if curr_sum == target:
                    self.result.append(path.copy())
                return

            path.append(candidates[i])
            dfs(i+1,curr_sum+candidates[i],path)
            path.pop()

            while i+1 <len(candidates) and candidates[i] == candidates[i+1]:
                i = i+1
            dfs(i+1,curr_sum,path)

        dfs(0, 0,[])
        return self.result