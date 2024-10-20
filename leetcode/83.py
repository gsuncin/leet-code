# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return dummy

    
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
print(sol.deleteDuplicates(sol.create_list_node([1, 1, 2])))  # [1,2]
# print(sol.deleteDuplicates([1,1,2,3,3]))  # [1,2,3]