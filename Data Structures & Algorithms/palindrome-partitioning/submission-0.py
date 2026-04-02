class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def is_palindrom(p):
            l=0
            r = len(p)-1
            while l<r:
                if p[l]!=p[r]:
                    return False
                l+=1
                r-=1

            
            return True

            
        def recur(s_,path,s):
            if ''.join(path)==s:
                result.append(path.copy())
                print(path,'1', s_)
                return 
            # if len(path)==3:
            #     print(path,'2')
            #     return 
            print(path,'3', s_)
            for pos in (range(len(s_))):
                if is_palindrom(s_[:pos+1]):
                    path.append(s_[:pos+1])
                    
                    recur(s_[pos+1:],path,s)

                    path.pop()

            
            
            





        # strng = [i for i in s]

        # for pos in range(len(strng)):

        recur( s[:],[],s)
        print(result)
        return result