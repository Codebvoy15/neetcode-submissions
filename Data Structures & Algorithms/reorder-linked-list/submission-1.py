# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find the middle of the list 

        fast = head
        slow = head 

        while fast and fast.next :
            slow = slow.next
            fast=fast.next.next

        second = slow.next  # this is the mid 
        slow.next = None

        #reverse the list 
        curr = second
        prev = None

        while curr:
            #save the next of current node 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node


        # merge the lists

        first = head
        second = prev

        while second : 
            f_next = first.next
            s_next = second.next

            first.next = second
            second.next = f_next 

            first = f_next
            second = s_next


