class Solution:
    def isHappy(self, n: int) -> bool:
        
        def Happy(n,past):
            if n in past:
                return False
            past.add(n)
            new_n = 0
            
            while n:
                new_n+= (n%10)**2
            
                n = n//10
            # print(past,new_n)
            if new_n == 1:
                return True
            
            return Happy(new_n,past)
    
        return Happy(n,set())

