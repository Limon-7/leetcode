# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node, curr_node = head, head.next
        prev_critical, last_critical = None, None
        i = 1
        min_dist, max_dist = float("inf"), -1

        while curr_node.next:
            if curr_node.val > max(
                prev_node.val, curr_node.next.val
            ) or curr_node.val < min(prev_node.val, curr_node.next.val):
                if not prev_critical:
                    prev_critical = i

                else:
                    max_dist = i - prev_critical
                    min_dist = min(min_dist, i - last_critical)
                last_critical = i

            i += 1
            prev_node = curr_node
            curr_node = curr_node.next

        return [min_dist, max_dist] if prev_critical != last_critical else [-1, -1]
