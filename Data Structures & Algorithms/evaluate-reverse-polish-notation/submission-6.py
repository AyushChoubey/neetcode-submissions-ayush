class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in  tokens:
            if i not in ['+', '-', '*','/']:
                stack.append(int(i))
            else:
                 
                        # print(stack)
                    
                        if i == "+":
                            stack.append(int(stack.pop())+ int(stack.pop()))
                        elif i == "-":
                             a = int(stack.pop())
                             stack.append(int(stack.pop())-a )
                        elif i == "*":
                             stack.append(int(stack.pop())* int(stack.pop()))
                        elif i == "/":
                             a = int(stack.pop())
                             b = int(stack.pop())
                             stack.append(int(b/a))
        # print(stack)
        return stack[0]
