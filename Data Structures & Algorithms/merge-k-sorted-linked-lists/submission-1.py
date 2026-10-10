import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        tail = dummy
        while heap:                              # replaces "if mi == -1: break"
            val, i, node = heapq.heappop(heap)   # replaces the for-loop scan
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))  # replaces lists[mi] = lists[mi].next
        return dummy.next