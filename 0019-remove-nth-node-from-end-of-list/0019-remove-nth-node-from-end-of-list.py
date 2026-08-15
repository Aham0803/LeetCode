# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force
        # length = 0
        # temp = head
        # while(temp != None):
        #     length += 1
        #     temp = temp.next
        # if length == n:
        #     prev_temp = head.next
        #     del head
        #     return prev_temp   
        # curr_len = length-n
        # current = 1
        # temp = head
        # while(current < curr_len):
        #     temp = temp.next
        #     current += 1
        # temp.next = temp.next.next
        # return head

        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next

        while(fast.next != None):
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
        

           
