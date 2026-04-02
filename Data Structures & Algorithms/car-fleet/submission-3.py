# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

#         stack = []
#         # stack.append([position[0],speed[1]])
#         dist_speed = [[position[i],speed[i]] for i in range(len(position))]
#         sorted_ds = sorted(dist_speed, key=lambda x: x[0])
#         stack.append(sorted_ds[0])
#         for i in range(1,len(position)):
#             # print(stack,sorted_ds[i])
#             if stack[-1][1]- sorted_ds[i][1] != 0:
#                 pos_meet = (sorted_ds[i][0]*stack[-1][1] - stack[-1][0]* sorted_ds[i][1])/(stack[-1][1]- sorted_ds[i][1])
#                 # print(stack,sorted_ds[i],pos_meet)
#                 while stack and 0<=pos_meet<= target and stack[-1][1]>sorted_ds[i][1]:
#                     stack.pop(-1)
#                     if stack and stack[-1][1]- sorted_ds[i][1] != 0:
#                         pos_meet = (sorted_ds[i][0]*stack[-1][1] - stack[-1][0]* sorted_ds[i][1])/(stack[-1][1]- sorted_ds[i][1])
#                     else: pos_meet = target+1
#                 stack.append(sorted_ds[i])
#             else:
#                 stack.append(sorted_ds[i])



#         return len(stack)

# Better Alternative:
# Instead of calculating pos they meet we calculate the time it will take to 
# reach the target if a car is ahead and takes longer time than the prev car then they 
# will definately meet before target so instead of checking pos we check time to reavh target 
# and compare it
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        
        time_pos = [[position[i], (target- position[i])/speed[i]] for i in range(len(position))]
        sorted_ds = sorted(time_pos, key=lambda x: x[0])

        # print(sorted_ds)
        for i in range(0,len(position)):
            # print(stack)
            while stack and stack[-1][1]<=sorted_ds[i][1]:
                    stack.pop(-1)
            stack.append(sorted_ds[i])
            



        return len(stack)