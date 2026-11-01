
import heapq

class Solution:
    def mergeKLists(self, lists):

        # Step 1: Initialize Min Heap
        heap = []

        # Step 2: Insert the head of every non-empty list
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # Step 3: Create dummy node and tail
        dummy = ListNode(0)
        tail = dummy

        # Step 4: Process the heap
        while heap:

            # Extract the smallest node
            value, i, node = heapq.heappop(heap)

            # Connect node to merged list
            tail.next = node

            # Move tail forward
            tail = tail.next

            # Insert the next node from the same list
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        # Step 5: Return merged linked list
        return dummy.next
