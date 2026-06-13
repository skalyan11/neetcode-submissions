# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while list1 or list2:
            a = b = float('inf')
            if list1:
                a = list1.val
            if list2:
                b = list2.val
            if a < b:
                curr.next = ListNode(a)
                list1 = list1.next
            else:
                curr.next = ListNode(b)
                list2 = list2.next
            
            curr = curr.next
        return dummy.next
                
        

