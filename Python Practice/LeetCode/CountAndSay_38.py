class Solution:
    def countAndSay(self, n: int) -> str:
        number_off = "1"    #初始报数序列

        for i in range(1, n):
            number_off = self.next_num(number_off)

        return number_off

    def next_num(self, previous_number_off):
        number_off = ""
        length = len(previous_number_off)  # 前一报数序列的长度
        i = 0

        while i < length:
            counter = 1  # 计数器——记录连续数字的个数
            while i < length - 1 and previous_number_off[i] == \
                    previous_number_off[i + 1]:
                counter += 1
                i += 1
            number_off += (str(counter) + previous_number_off[i])
            i += 1

        return number_off