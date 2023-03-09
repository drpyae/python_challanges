# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      """
      To detect the beginning of a cycle in a linked list, we can use the Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm.
      This algorithm works by using two pointers: a slow pointer that moves one node at a time, and a fast pointer that moves two nodes at a time. 
      If there is a cycle in the linked list, then the two pointers will eventually meet at some node in the cycle.
      To find the beginning of the cycle, we need to determine the length of the cycle and the distance between the head of the list and the beginning of the cycle. 
      Once we have these two values, we can move one pointer from the head of the list and the other pointer from the node where the two pointers met in the cycle. 
      When these two pointers meet, the node they are pointing to is the beginning of the cycle.
      """
        if not head or not head.next:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if not slow or not fast or fast.next is None:
            return None  # no cycle found

        # determine the length of the cycle
        cycle_len = 1
        node = slow
        while node.next != slow:
            node = node.next
            cycle_len += 1

        # determine the distance between the head and the beginning of the cycle
        node1 = node2 = head
        for i in range(cycle_len):
            node2 = node2.next

        while node1 != node2:
            node1 = node1.next
            node2 = node2.next

        return node1  # node1 is the beginning of the cycle
