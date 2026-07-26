# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr = head

        while curr: 
            if curr.val == "seen": 
                return True
            curr.val = "seen"
            curr = curr.next
        
        return False
        