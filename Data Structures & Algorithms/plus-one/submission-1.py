class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        else:
            i = len(digits)
            while digits[i-1]== 9:
                digits[i-1] = 0
                i-=1
            print(digits,i)
            if i != 0 :
                digits[i-1]+=1
            else:
                digits[i] = 0
                print(digits)
                digits.insert(0, 1)
                print(digits)
            return digits