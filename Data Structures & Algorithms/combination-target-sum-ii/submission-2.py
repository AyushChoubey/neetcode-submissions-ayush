class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        def get_comb(target,current_sum,path,candidates,visited):
            if current_sum >= target:
                if current_sum == target:
                    self.result.append(path.copy())
                return 
            
            for i in range(len(candidates)):
                picked = candidates[i]
                if picked not in visited:
                    visited.append(picked)
                    path.append(picked)
                    current_sum += picked
                    get_comb(target,current_sum,path,candidates[i+1:],[])
                    path.pop()
                    current_sum -=picked

        candidates.sort()
    
        get_comb(target,0,[],candidates,[])
        return self.result

