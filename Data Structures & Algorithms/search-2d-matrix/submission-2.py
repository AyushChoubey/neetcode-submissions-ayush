class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_list = []
        for i in matrix:
            new_list.extend(i)
        # print(new_list)

        l = 0
        r = len(new_list) -1 
        while l<=r:
            m = l+(r-l)//2
            # print(m,new_list[m],target,l,r)
            if new_list[m] < target:
                
                l = m+1
            elif new_list[m]>target:
                r= m-1
            else:
                # print('yay')
                return True
        return False
