# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #brute force
        # arr = []
        # temp = head
        # while(temp):
        #     arr.append(temp)
        #     temp = temp.next
        # left = 0
        # right = len(arr)-1
        # while(left < right):
        #     arr[left].next = arr[right]
        #     left += 1
        #     arr[right].next = arr[left]
        #     right -= 1
        # arr[left].next = None

        # optimal
        slow = head
        fast = head

        #finding middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # merging
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
