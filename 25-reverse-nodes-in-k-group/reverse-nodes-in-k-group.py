# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        count = 0
        curr = head

        while curr:
            curr = curr.next
            count += 1
            if count == k:
                break
        
        if count < k:
            return head
        
        curr = head
        prev = None

        currGroupHead = head

        for i in range(k):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        
        head.next = self.reverseKGroup(curr,k)

        return prev
    
        