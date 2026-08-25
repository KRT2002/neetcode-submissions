# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # let's count the number of nodes in linked list first
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        
        removeIndex = N - n
        if removeIndex == 0:
            return head.next
        
        cur = head
        for i in range(N):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
