# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 处理空链特殊情况或确定结果链头节点
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            first_node = l1 #结果链头结点
            l1 = l1.next
        else:
            first_node = l2 #结果链头结点
            l2 = l2.next
        first_node.next = None
        result = first_node #追踪结果链

        # 完成结果链
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next

        while l1 != None:
            result.next = l1
            l1 = l1.next
            result = result.next

        while l2 != None:
            result.next = l2
            l2 = l2.next
            result = result.next

        return first_node