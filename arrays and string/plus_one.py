class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1=""
        list1 = []
        for i in range(0, len(digits)):
            str1 += str(digits[i])
        num = int(str1)
        num2 = (num+1)
        while(num2):
            rem = num2 % 10
            list1.append(rem)
            num2 = num2 // 10
        list1.reverse()
        
        return list1
                