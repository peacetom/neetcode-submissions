class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self._get_node_helper(index, self.head).val


    def get_node(self, index: int) -> ListNode:
        if index < 0 or index >= self.size:
            return -1
        return self._get_node_helper(index, self.head)


    def _get_node_helper(self, index, node):
        if node is None:
            return -1
        if index == 0:
            return node
        return self._get_node_helper(index - 1, node.next)
        

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
        if index == 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)

        node_next = self.get_node(index)
        new_node = ListNode(val)
        node_prev = node_next.prev
        new_node.next = node_next
        node_prev.next = new_node
        new_node.prev = node_prev
        node_next.prev = new_node
        self.size += 1

        return None


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        
        if index == 0:
            node_to_remove = self.head
            self.head = self.head.next
            node_to_remove.next = None
            self.head.prev = None
        elif index == self.size - 1:
            node_to_remove = self.tail
            self.tail = self.tail.prev
            node_to_remove.prev = None
            self.tail.next = None
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