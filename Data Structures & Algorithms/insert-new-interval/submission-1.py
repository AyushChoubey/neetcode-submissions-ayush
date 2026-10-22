class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        #binary search

        # take out the starts of each intervals:
        start = [i[0] for i in intervals ]
        key = newInterval[0]

        #binary search 
        l = 0 
        r = len(start)-1
        m = -1

        while l<=r:

            m = (l+r)//2

            if key>intervals[m][0]:
                l = m+1
            
            else:
                r = m-1

            # else:
            #     if intervals[m][0] >=newInterval[1]:
            #         m = m-1
            #         break
            #     if intervals[m][0] < newInterval[1]:
            #         m = m+1
            #         break
            

        intervals.insert(l,newInterval)

        merge_idx = []
        res = []
        

        for i in range(len(intervals)):
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1],intervals[i][1])

        # print(res)
        return res

        # def merger(intervals):


        #     for i range(len(intervals)-1):
        #         if intervals[i][1] > intervals[i+1][0]:

        #             interval.insert(i[interval[i][0],interval[i][1]])


            




            
                


        