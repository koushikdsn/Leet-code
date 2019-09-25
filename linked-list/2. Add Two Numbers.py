"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        node = root
        while l1.next or l2.next:
            s = (l1.next.val if l1.next else 0) + (l2.next.val if l2.next else 0) + carry
            node.next = ListNode(s % 10)
            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next
            node = node.next
            carry = s // 10
        if carry:
            node.next = ListNode(carry)
        return root