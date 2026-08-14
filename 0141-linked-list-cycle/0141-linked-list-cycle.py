# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        my_set =[]
        while(temp != None):
            if(temp in my_set):
                return True
            else:
                my_set.append(temp)
                temp = temp.next
        
        return False