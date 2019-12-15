class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        while len(nums) > 1:
            if nums.pop() != nums.pop(0):
                return False
            
        return True
        