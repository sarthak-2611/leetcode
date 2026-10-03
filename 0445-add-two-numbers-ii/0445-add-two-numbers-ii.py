# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def rev(head):
            prev = None
            while head:
                head.next, prev, head = prev, head, head.next
            return prev
        
        l1, l2, carry, head = rev(l1), rev(l2), 0, None
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            head, carry = ListNode(carry % 10, head), carry // 10
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return head
