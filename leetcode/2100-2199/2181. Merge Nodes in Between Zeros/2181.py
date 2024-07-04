# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            tmp = curr.next
            curr = curr.next

            while curr.next.val:
                tmp.val += curr.next.val
                curr = curr.next
            curr = curr.next
            tmp.next = curr.next

        return head.next
