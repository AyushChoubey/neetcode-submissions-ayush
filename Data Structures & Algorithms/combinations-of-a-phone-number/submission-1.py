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
        def get_letter_comb(num_dict,curr_dig,digits,path):

            if len(path) == len(digits):
                if len(digits)!=0:
                    self.result.append(''.join(path.copy()))
            
            for  i in range(len(curr_dig)):
                if curr_dig[i] in num_dict:
                    for j in  range (len(num_dict[curr_dig[i]])):
                            # print(path,num_dict[curr_dig[i]][j])
                            path.append(num_dict[curr_dig[i]][j])

                            get_letter_comb(num_dict,curr_dig[i+1:],digits,path)
                            path.pop()

        get_letter_comb(num_dict,digits[:],digits,[])

        print(self.result)
        return self.result