# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(next=head.next)
        node = head
        while node and node.next:
            nxt = node.next
            nxt2 = nxt.next
            nxt.next = node
            node.next = nxt2.next if nxt2 and nxt2.next else nxt2
            node = nxt2
        return dummy.next