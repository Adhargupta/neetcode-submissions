class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = int(num1)
        int_num2 = int(num2)
        int_num3 = int_num1*int_num2
        st = str(int_num3)
        return st