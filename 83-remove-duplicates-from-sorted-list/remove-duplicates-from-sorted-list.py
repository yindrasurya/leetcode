# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if head==None:
            return head
        while(temp.next!=None):
            temp1=temp.next
            if(temp.val==temp1.val):
                temp.next=temp1.next
                temp1.next=None 
            else:
                temp=temp.next
            if(temp==None):
                break
        return head
             