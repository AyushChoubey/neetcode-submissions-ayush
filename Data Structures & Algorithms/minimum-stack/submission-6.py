class MinStack:

    def __init__(self):
        self.stack = []
        # self.mini = float('inf')
        self.min_stack = []
        self.min_ = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if self.min_stack:
        # self.min_ = min(val,self.min_)
        # self.min_stack.append(self.min_)

        if self.min_stack:

            self.min_ = min(val,self.min_)
            self.min_stack.append(self.min_)
        else:
            self.min_ = val
            self.min_stack.append(self.min_)

       
            

        
        

    def pop(self) -> None:
        self.stack.pop()
        
        self.min_stack.pop()
        if self.min_stack:
            self.min_ = self.min_stack[-1]
        # return popped_val

        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        # print(self.min_stack)
        return self.min_

        
