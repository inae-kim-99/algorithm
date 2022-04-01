# https://leetcode.com/problems/swap-nodes-in-pairs/
# leetcode 24 : Swap Nodes in Pairs
# LEVEL : Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        answer = head.next
        node1 = ListNode(0, head)

        while node1.next and node1.next.next:
            node2 = node1.next
            node3 = node2.next
            node4 = node3.next

            node2.next = node4
            node3.next = node2
            node1.next = node3

            node1 = node2

        return answer

