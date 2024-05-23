# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"[{self.val}] > {self.next}"



class Solution(object):
    def reverseList(self, head):
        prev_node = None
        current_code = head
        while current_code:
            next_node = current_code.next
            current_code.next = prev_node
            prev_node = current_code
            current_code = next_node
        return prev_node



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

print(node1)

solution = Solution().reverseList(node1)

print(solution)