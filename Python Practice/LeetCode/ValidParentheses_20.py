class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        else:
            stack = ''  #模拟一个栈
            index = -1  #模拟栈顶指针
            for i in range(0, int(len(s))):
                if s[i] == '(' or s[i] == '[' or s[i] == '{':
                    stack += s[i]   #入栈
                    index += 1  #栈顶指针+1
                elif index < 0:
                    return False    #遍历完前发生栈空则失败
                elif s[i] == ')':
                    if stack[index] == '(':
                        stack = stack[:-1]  #出栈
                        index -= 1  #栈顶指针-1
                    else:
                        return False
                elif s[i] == ']':
                    if stack[index] == '[':
                        stack = stack[:-1]  # 出栈
                        index -= 1  # 栈顶指针-1
                    else:
                        return False
                elif s[i] == '}':
                    if stack[index] == '{':
                        stack = stack[:-1]  # 出栈
                        index -= 1  # 栈顶指针-1
                    else:
                        return False
            if index < 0:
                return True
            else:
                return False