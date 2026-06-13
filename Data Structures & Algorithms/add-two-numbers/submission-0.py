# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       o = ListNode(0)
       l3 = o
       carry = 0
       while l1 or l2 or carry:
            l = l1.val if l1 else 0
            ls = l2.val if l2 else 0
            s = l + ls + carry
            carry = s // 10
            l3.next = ListNode(s % 10)
            l3 = l3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
       return o.next
            


            
