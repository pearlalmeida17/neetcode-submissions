# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curt = head


        while curt :
            nxt = curt.next
            curt.next = prev
            prev = curt
            curt = nxt
        
        return prev



        