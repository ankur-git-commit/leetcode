# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ll_length = 0
        cur = head
        while cur:
            ll_length += 1
            cur = cur.next

        prev = None
        cur = head
        while cur:
            if ll_length == n and prev:
                prev.next = cur.next
                return head
            elif ll_length == n and not prev:
                if not cur.next:
                    return None
                else:
                    return cur.next
            ll_length -= 1
            prev = cur
            cur = cur.next
