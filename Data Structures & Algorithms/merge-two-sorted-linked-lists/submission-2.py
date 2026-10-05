# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()
        # tail = dummy
        # current1 = list1
        # current2 = list2
        # while current1 and current2:
        #     if current1.val < current2.val:
        #         tail.next = current1
        #         current1 = current1.next
        #     else:
        #         tail.next = current2
        #         current2 = current2.next
        #     tail = tail.next
        # if current1:
        #     tail.next = current1
        # if current2:
        #     tail.next = current2
        # return dummy.next

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


