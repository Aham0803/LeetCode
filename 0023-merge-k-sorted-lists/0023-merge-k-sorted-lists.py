# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr =[]
        for head in lists:
            temp = head

            while temp:
                arr.append(temp.val)
                temp = temp.next

        arr.sort()

        dummy = ListNode()
        curr = dummy

        for value in arr:
            curr.next = ListNode(value)
            curr = curr.next
        
        return dummy.next

        