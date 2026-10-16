# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self,head,target):
        dummy=curr=ListNode()
        dummy.next=head
        while curr.next:
            if curr.next.val!=target:
                curr=curr.next
            else:
                curr.next=curr.next.next
        return dummy.next