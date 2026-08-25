# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1, cur_l2 = l1, l2
        carry = 0
        dummy_head = ListNode(0)
        dummy = dummy_head

        while cur_l1 or cur_l2 or carry:
            v1 = cur_l1.val if cur_l1 else 0
            v2 = cur_l2.val if cur_l2 else 0

            total = v1 + v2 + carry

            carry = total // 10
            val_in = total % 10

            new_node = ListNode(val_in)
            dummy.next = new_node
            dummy = dummy.next
            cur_l1 = cur_l1.next if cur_l1 else None
            cur_l2 = cur_l2.next if cur_l2 else None
        
        return dummy_head.next
