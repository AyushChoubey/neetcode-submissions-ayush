class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        nums = ["(",")"]
        def get_parenth(nums,path,count_dict):
            if len(path) == 2*n :
                print(count_dict,path)
                self.result.append(''.join(path))
                return
            
            
            for i in range(len(nums)):
                picked = nums[i]
                count_dict[picked]+=1
              
                if count_dict["("]>= count_dict[")"]  and count_dict[picked]<=n: 
                    path.append(picked)
                   
                    get_parenth(nums,path,count_dict)
                    path.pop()

                count_dict[picked]-=1
        count_dict  = {"(":0,")":0}
        get_parenth(nums,[],count_dict)
        
        print(self.result)
        return self.result
            
        
        