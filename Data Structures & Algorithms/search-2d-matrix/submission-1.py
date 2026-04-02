class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_r = 0
        r_r = len(matrix)-1
        
       
        # cnt=0
        while l_r<=r_r:
            # print(l_r,m_r,r_r)
            m_r = l_r+(r_r-l_r)//2
            print(l_r,m_r,r_r)
            if matrix[m_r][0] > target:
                r_r = m_r-1
                print('---1')
               
            elif matrix[m_r][0] < target:
                # print('---2')
                if matrix[m_r][-1] > target:
                    print('---3',matrix[m_r][-1])
                    l_c = 0
                    r_c = len(matrix[m_r])-1
                    while l_c < r_c:

                        m_c = l_c+(r_c-l_c)//2
                        print(matrix[m_r][m_c])
                        if matrix[m_r][m_c] >target:
                            r_c = m_c-1
                        elif matrix[m_r][m_c] <target:
                            l_c = m_c+1
                        else:
                            return True
                    return False

                elif matrix[m_r][-1] < target:
                    # print('---4')
                    l_r = m_r +1
                else :
                    return True


                

               

            else:
                # print("yaya")
                return True
            # cnt+=1
        # print(m_r,l_r,r_r)

        return False
            