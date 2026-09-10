"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head

        og_to_copy = {None : None}

        while curr:
            og_to_copy[curr] =  Node(curr.val)
            curr = curr.next

        curr = head 
        while curr:
            og_to_copy[curr].next = og_to_copy[curr.next]
            og_to_copy[curr].random = og_to_copy[curr.random]

            curr = curr.next

        return og_to_copy[head]

        
        