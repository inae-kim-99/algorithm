# https://leetcode.com/problems/intersection-of-two-linked-lists/
# leetcode 160 : Intersection of Two Linked Lists
# LEVEL : Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def moveNode(self, node: ListNode, number: int):
        for i in range(number):
            node = node.next
        return node

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA, lengthB = 1, 1
        nodeA, nodeB = headA, headB

        while nodeA.next != None:
            lengthA += 1
            nodeA = nodeA.next
        while nodeB.next != None:
            lengthB += 1
            nodeB = nodeB.next

        if nodeA != nodeB:
            return None
        else:
            if lengthA < lengthB:
                headB = self.moveNode(headB, lengthB-lengthA)
            else:
                headA = self.moveNode(headA, lengthA-lengthB)

            while headA != None:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
