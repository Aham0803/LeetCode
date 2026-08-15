# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force
        if head == None or head.next == None:
            return head
        
        values =[]
        temp = head
        while temp != None:
            values.append(temp.val)
            if temp.next == None:
                break
            temp = temp.next.next
            
        temp = head.next
        while temp != None:
            values.append(temp.val)
            if temp.next is None:
                break
            temp =  temp.next.next
        
        temp = head
        index = 0
        while(temp is not None):
            temp.val = values[index]
            index += 1
            temp = temp.next
        return head
        