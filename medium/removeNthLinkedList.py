class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nums = []
        curr = head
        # Traverse through linked list and store values in array
        while curr != None:
            nums.append(curr.val)
            curr = curr.next
        # pop from list
        nums.pop(len(nums)-n)
        
        answer = dummy = ListNode(0)
        for item in nums:
            dummy.next = ListNode(item)
            dummy = dummy.next
        
        return answer.next