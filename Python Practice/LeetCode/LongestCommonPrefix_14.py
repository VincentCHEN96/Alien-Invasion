class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""
        else:
            flag = False    #匹配结果标志位
            i = len(strs[0])    #以第一个字符串为参考进行匹配查找
            while i >= 0:
                front_str = strs[0][:i] #待匹配的前缀字符串
                for str in strs:
                    try:
                        if str.index(front_str) != 0:
                            flag = False
                            i -= 1
                            break
                    except ValueError:
                        flag = False
                        i -= 1
                        break
                    flag = True
                if flag:
                    return front_str
            return ""