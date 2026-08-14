# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #brute force
        # temp = head
        # my_set =[]
        # while(temp != None):
        #     if(temp in my_set):
        #         return True
        #     else:
        #         my_set.append(temp)
        #         temp = temp.next
        
        # return False

        # optimal
        slow = head
        fast = head
        while( fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False