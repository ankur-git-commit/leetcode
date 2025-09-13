# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive solution
        # time - O(n)
        # space - O(n)
        return self.recursive_revList(head)

    def recursive_revList(self, cur, prev=None):
        if not cur:
            return prev
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        return self.recursive_revList(cur, prev)


        # Iterative solution 
        # time - O(n)
        # space - O(1)

        # prev = None
        # cur = head
        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        
        # return prev