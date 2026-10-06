class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or self.size <= index:
            return -1

        curr = None

        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index - 1):
                curr = curr.prev

        return curr.val

    
    def get_node(self, index: int) -> ListNode | None:
        if index < 0 or self.size <= index:
            return None

        curr = None

        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index - 1):
                curr = curr.prev

        return curr
        
        
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        
        new_node = ListNode(val)

        if index == 0:
            if self.size == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            node_idx = self.get_node(index)
            node_prev = node_idx.prev
            node_prev.next = new_node
            node_idx.prev = new_node
            new_node.prev = node_prev
            new_node.next = node_idx
        self.size += 1
        return None


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        
        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                new_head = self.head.next
                self.head.next = None
                new_head.prev = None
                self.head = new_head
        elif index == self.size - 1:
            new_tail = self.tail.prev
            self.tail.prev = None
            new_tail.next = None
            self.tail = new_tail
        else:
            node_to_remove = self.get_node(index)
            prev_node = node_to_remove.prev
            next_node = node_to_remove.next
            prev_node.next = next_node
            next_node.prev = prev_node
        self.size -= 1
        return None


class ListNode:

    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)