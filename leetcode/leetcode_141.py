# https://leetcode.com/problems/linked-list-cycle/
# leetcode 141 : Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_list = []
        while head != None:
            if head in node_list:
                return True
            else:
                node_list.append(head)
            head = head.next
        return False
