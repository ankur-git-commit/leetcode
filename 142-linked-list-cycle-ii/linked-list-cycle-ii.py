# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map = {}
        pos = 0
        curr = head

        while curr:
            if curr in hash_map:
                # We’ve seen this node before → cycle entry
                return curr
            hash_map[curr] = pos
            pos += 1
            curr = curr.next

        return None