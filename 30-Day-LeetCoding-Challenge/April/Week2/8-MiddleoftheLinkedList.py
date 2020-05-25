"""
Given a non-empty, singly linked list with head node "head", return a middle node
of linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# O(n)
# Count the number of elements
# find the middle index
# go to the index and return that node
def middleNode0(head: ListNode) -> ListNode:
    # Find the number of elements in the list
    copyHead = head
    size = 1
    while copyHead.next != None:
        size += 1
        copyHead = copyHead.next
    # Find the middle index
    mid = size//2 + 1
    # Get the middle element
    count = 1
    res = head
    while count != mid:
        res = res.next
        count += 1
    return res


# O(n/2)
# Have to pointers where one is moving twice as fast as the other
# when the fast one reaches the end you know that the other one must be in
# the middle
def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow
