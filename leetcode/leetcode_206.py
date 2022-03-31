# https://leetcode.com/problems/reverse-linked-list/
# leetcode 206 : Reverse Linked List
# LEVEL : Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        next_node = head.next
        head.next = None
        while next_node:
            next_next_node = next_node.next
            next_node.next = head
            
            head, next_node = next_node, next_next_node
        
        return head
            
        