# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        prev = None
        while curr1 or curr2:
            if curr1 is None:
                prev.next = ListNode(0)
                curr1 = prev.next

            s = curr1.val + (curr2.val if curr2 else 0)
            if s >= 10:
                if curr1.next is None:
                    curr1.next = ListNode(s // 10)
                else:
                    curr1.next.val += s // 10
            curr1.val = s % 10

            prev = curr1
            curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return l1