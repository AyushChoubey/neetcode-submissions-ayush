class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9':['w','x','y','z']}
        self.result = []
        def get_letter_comb(num_dict,i,digits,path):

            if len(path) == len(digits):
                if len(digits)!=0:
                    self.result.append(''.join(path.copy()))
                return 
            # print(path,i,len(path),len(digits))
            # for  i in range(len(curr_dig)):
            if digits[i] in num_dict:
                for j in  range (len(num_dict[digits[i]])):
                        # print(path,num_dict[curr_dig[i]][j])
                        path.append(num_dict[digits[i]][j])

                        get_letter_comb(num_dict,i+1,digits,path)
                        path.pop()

        get_letter_comb(num_dict,0,digits,[])

        # print(self.result)
        return self.result