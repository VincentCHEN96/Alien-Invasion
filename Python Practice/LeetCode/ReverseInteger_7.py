class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))  #转换成字符串列表利用头尾指针做对调
        # print(x)    #Testing Code
        head = 0    #头指针
        tail = len(x) - 1   #尾指针

        #过滤符号位
        if x[head] == '-':
            head += 1
        #对调元素
        while head < tail:
            temp = x[head]
            x[head] = x[tail]
            x[tail] = temp
            head += 1
            tail -= 1
        result = int("".join(x))  #将字符串列表先转成字符串后转成整形数（自动去掉首部0）
        #判断输出结果是否超出32位有符号整数的范围
        if result >= -(2 ** 31) and result <= (2 ** 31) - 1:
            return result
        else:
            return 0