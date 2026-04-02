class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        stack.append([temperatures[0],0])
        result = [0]*len(temperatures)

        for i in range (1,len(temperatures)):
            
                # print(stack)
                if temperatures[i]<=stack[-1][0]:
                    stack.append([temperatures[i],i])
                else:
                    while stack and temperatures[i]>stack[-1][0]:
                        a = stack.pop(-1)
                        result[a[1]] = i- a[1]
                    stack.append([temperatures[i],i])
            

        # print(result,stack)
        return result





            

        