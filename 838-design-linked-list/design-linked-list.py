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
        if index < 0:
            return

        new_node = ListNode(val)
        if not self.head:
            if index == 0:
                self.head = new_node
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        for _ in range(index - 1):
            if curr.next is None:
                return
            curr = curr.next

        if curr.next is None:
            curr.next = new_node
            self.tail = new_node
        else:
            new_node.next = curr.next
            curr.next = new_node

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