class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        self.printList()
        if not self.head:
            return -1 
        cur = self.head
        while cur:
            if index == 0:
                return cur.val
            cur = cur.next
            index -= 1
        return -1

    def addAtHead(self, val: int) -> None:
        Node = ListNode(val)
        if not self.head:
            self.head = Node
            return
        Node.next = self.head
        self.head = Node
        return        

    def addAtTail(self, val: int) -> None:
        Node = ListNode(val)
        if not self.head:
            self.head = Node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        prev = self.head
        for _ in range(index - 1):
            if not prev:
                return
            prev = prev.next
        
        if not prev:
            return
        
        Node = ListNode(val)
        Node.next = prev.next
        prev.next = Node
        return

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0 and self.head:
            self.head = self.head.next
            return
        cur = self.head
        prev = None
        while cur:
            if index == 0:
                prev.next = cur.next
                return
            index -= 1
            prev = cur
            cur = cur.next
        return 
    def printList(self):
        cur = self.head
        values = []
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(values) if values else "Empty")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtself.head(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)