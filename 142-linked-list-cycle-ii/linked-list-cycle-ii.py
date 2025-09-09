# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # without O(n) memory space using two-pointer(slow and fast)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


        # using hash_map
        # hash_map = {}
        # pos = 0
        # curr = head

        # while curr:
        #     if curr in hash_map:
        #         # We’ve seen this node before → cycle entry
        #         return curr
        #     hash_map[curr] = pos
        #     pos += 1
        #     curr = curr.next

        # return None