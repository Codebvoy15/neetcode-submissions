# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = l1 
        second = l2 
        carry = 0 
        dummy = ListNode(0)
        cur = dummy

        while first or second or carry:
            if first : 
                x = first.val 
            else : 
                x = 0 
            
            if second: 
                y = second.val

            else: 
                y = 0



            total = x + y + carry
            digit = total % 10
            carry = total // 10

            cur.next = ListNode(digit)
            cur = cur.next

            if first:
                first = first.next
            if second:
                second = second.next

        return dummy.next
