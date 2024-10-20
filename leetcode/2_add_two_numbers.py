"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
"""

# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum1 = []
        while l1:
            sum1.append(l1.val)
            l1 = l1.next
        sum2 = []
        while l2:
            sum2.append(l2.val)
            l2 = l2.next
        sum1.reverse()
        sum2.reverse()
        sum1 = "".join(str(n) for n in sum1)
        sum2 = "".join(str(n) for n in sum2)
        result = [int(n) for n in str(int(sum1) + int(sum2))]
        result.reverse()
        result = self.create_list_node(result)
        return result
    
    def create_list_node(self, values: list) -> Optional[ListNode]:
        if not values:
            return None
        initial = ListNode(values[0])
        current = initial
        for val in values[1::]:
            current.next = ListNode(val)
            current = current.next
        return initial


sol = Solution()
l1 = sol.create_list_node([2, 4, 3])
l2 = sol.create_list_node([5, 6, 4])

sol.addTwoNumbers(l1, l2)
