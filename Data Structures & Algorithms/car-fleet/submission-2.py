class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        # stack.append([position[0],speed[1]])
        dist_speed = [[position[i],speed[i]] for i in range(len(position))]
        sorted_ds = sorted(dist_speed, key=lambda x: x[0])
        stack.append(sorted_ds[0])
        for i in range(1,len(position)):
            # print(stack,sorted_ds[i])
            if stack[-1][1]- sorted_ds[i][1] != 0:
                pos_meet = (sorted_ds[i][0]*stack[-1][1] - stack[-1][0]* sorted_ds[i][1])/(stack[-1][1]- sorted_ds[i][1])
                # print(stack,sorted_ds[i],pos_meet)
                while stack and 0<=pos_meet<= target and stack[-1][1]>sorted_ds[i][1]:
                    stack.pop(-1)
                    if stack and stack[-1][1]- sorted_ds[i][1] != 0:
                        pos_meet = (sorted_ds[i][0]*stack[-1][1] - stack[-1][0]* sorted_ds[i][1])/(stack[-1][1]- sorted_ds[i][1])
                    else: pos_meet = target+1
                stack.append(sorted_ds[i])
            else:
                stack.append(sorted_ds[i])



        return len(stack)

            