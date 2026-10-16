class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Step 1: Count the nodes
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        # Step 2: Create a dummy node
        dummy = ListNode(0, head)

        # Step 3: Move to the node BEFORE the one to remove
        cur = dummy

        for i in range(length - n):
            cur = cur.next

        # Step 4: Skip the node we want to remove
        cur.next = cur.next.next

        # Step 5: Return the updated list
        return dummy.next