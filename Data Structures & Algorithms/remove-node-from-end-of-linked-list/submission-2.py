# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = 0
        start = head
        while start and start.next:
            start=start.next
            s+=1
        s+=1
        if(s == 1):
            return None
        if n == s:
            return head.next
        i = s - n
        start = head
        
        for _ in range(i-1):
            start = start.next
        start.next = start.next.next
        return head
