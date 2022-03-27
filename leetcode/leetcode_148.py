# https://leetcode.com/problems/sort-list/
# leetcode 148 : Sort List
# LEVEL : Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, node, length):
        if length <= 1:
            return node
        
        nodeA = node
        for i in range(length//2-1):
            node = node.next
        nodeB = node.next
        node.next = None

        nodeA = self.mergeSort(nodeA, length//2)
        nodeB = self.mergeSort(nodeB, length-length//2)
        
        return self.merge(nodeA, nodeB)
            
    def merge(self, nodeA, nodeB):
        startNode = ListNode()
        pointer = startNode
        while nodeA != None and nodeB != None:
            if nodeA.val < nodeB.val:
                pointer.next = nodeA
                nodeA = nodeA.next
            else:
                pointer.next = nodeB
                nodeB = nodeB.next
            pointer = pointer.next

        while nodeA != None:
            pointer.next = nodeA
            nodeA = nodeA.next
            pointer = pointer.next

        while nodeB != None:
            pointer.next = nodeB
            nodeB = nodeB.next
            pointer = pointer.next

        return startNode.next
        
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0

        node = head
        while node != None:
            length += 1
            node = node.next
            
        return self.mergeSort(head, length)
        
        