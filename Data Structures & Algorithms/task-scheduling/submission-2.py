import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = {}
        for i in tasks:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i] =1

        counter = [[0,-freq_dict[i],i] for i in freq_dict]
        
        heapq.heapify(counter)



         
        i = 0
        last_task = ''
        cnt = 0
        while tasks!=[]:
            # print(tasks,counter[0],cnt)
            # if last_task != counter[0][1]:
            if counter[0][0] ==0:
                tasks.remove(counter[0][2])
                counter[0][1] +=1
                cnt +=1
                for i in counter:
                    if i[0]>0:
                        i[0]-=1
                counter[0][0]= n
                last_task = counter[0][2]
            else: 
                cnt +=1
                for i in counter:
                    if i[0]>0:
                        i[0]-=1


            # else:

            #     cnt +=1
            #     for i in counter:
            #         if i[0]>0:
            #             i[0]-=1
            if counter[0][1] == 0:
                heapq.heappop(counter)
            heapq.heapify(counter)
        return cnt
                


                
                


        