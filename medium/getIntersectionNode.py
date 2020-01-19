# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr1, curr2 = headA, headB
        lenA, lenB = 0, 0
        while curr1:
            lenA += 1
            curr1 = curr1.next
        while curr2:
            lenB += 1
            curr2 = curr2.next   
            
        if lenA < lenB:
            for _ in range(lenB-lenA):
                headB = headB.next
        else:
            for _ in range(lenA-lenB):
                headA = headA.next
        
        while headA != headB:
            headA, headB = headA.next, headB.next
        
        return headA
            
        