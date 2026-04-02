class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        map_ = {'(':')','{':'}','[':']'}
        # if len(S) == 0:
        #     return False
        # stack.append(s[0])
        for i in s:
            if len(stack) ==0  :
                if i not in map_:
                    return False
                    
                stack.append(i)
                continue
            if i != map_[stack[-1]] :
                if i not in map_:
                    return False
                stack.append(i)
            else:
                stack.pop()
        print(stack)
        return not(bool(len(stack)))

