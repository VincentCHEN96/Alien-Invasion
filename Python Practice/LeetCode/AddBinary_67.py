class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1  #a的尾指针
        j = len(b) - 1  #b的尾指针
        result = [] #结果串列表
        carry = 0   #进位数

        while i >= 0 and j >= 0:
            result.insert(0, str(int(a[i]) + int(b[j]) + carry))
            if result[0] == '2':
                result[0] = '0'
                carry = 1
            elif result[0] == '3':
                result[0] = '1'
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1

        while i >= 0:
            result.insert(0, str(int(a[i]) + carry))
            if result[0] == '2':
                result[0] = '0'
                carry = 1
            elif result[0] == '3':
                result[0] = '1'
                carry = 1
            else:
                carry = 0
            i -= 1

        while j >= 0:
            result.insert(0, str(int(b[j]) + carry))
            if result[0] == '2':
                result[0] = '0'
                carry = 1
            elif result[0] == '3':
                result[0] = '1'
                carry = 1
            else:
                carry = 0
            j -= 1

        # 最后的进位数非0则加到最前面
        if carry == 1:
            result.insert(0, '1')

        return "".join(result)