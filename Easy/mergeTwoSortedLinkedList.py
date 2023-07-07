from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumy = ListNode()
        head = dumy
        while list1 and list2: #check for non-empty list
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1:
            head.next = list1
        elif list2:
            head.next = list2
        head = dumy.next #to avoid the 0 in dummy node move head to dummy next
        return head
# Test the code
sol = Solution()

# Create the linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)

list2 = ListNode(2)
list2.next = ListNode(2)
list2.next.next = ListNode(4)
list2.next.next.next = ListNode(5)
list2.next.next.next.next = ListNode(7)
list2.next.next.next.next.next = ListNode(8)

result = sol.mergeTwoLists(list1, list2)

# Print the values of the merged linked list
while result:
    print(result.val, end=" ")
    result = result.next
