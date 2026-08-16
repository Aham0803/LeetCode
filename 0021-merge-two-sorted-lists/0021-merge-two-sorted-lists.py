# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #brutte force
        arr =[]
        temp = list1
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        
        temp = list2
        while(temp):
            arr.append(temp.val)
            temp = temp.next
        
        arr.sort()

        dummy = ListNode()
        temp = dummy

        for num in arr:
            temp.next = ListNode(num)
            temp = temp.next
        
        return dummy.next


