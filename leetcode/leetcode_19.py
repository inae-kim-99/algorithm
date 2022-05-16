# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# leetcode 19 : Remove Nth Node From End of List
# LEVEL : Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(0, head)

        length = 0
        while head:
            head = head.next
            length += 1
        head = root

        for _ in range(length-n):
            head = head.next
        head.next = head.next.next

        return root.next
        