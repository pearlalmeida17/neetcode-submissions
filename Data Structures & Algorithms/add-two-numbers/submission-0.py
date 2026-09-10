# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0 

        a = ListNode
        b = ListNode()

        dummy = ListNode(0)

        curr = dummy

        a = l1
        b = l2

        while a or b or carry:

            v1 = a.val if a else 0
            v2 = b.val if b else 0

            total = carry + v1 + v2

            carry  = total // 10
            digit = total % 10 

            curr.next = ListNode(digit)
            curr = curr.next

            a = a.next if a else None
            b = b.next if b else None


        return dummy.next        

        
            

        