# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            current = head
            while list1 != None and list2 != None:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            if list1 == None:
                current.next = list2
            else:
                current.next = list1
            return head

# Runtime: 32 ms, faster than 92.77% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.3 MB, less than 49.98% of Python3 online submissions for Merge Two Sorted Lists.

# Time complexity: O(n)
# Space complexity: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# print the linked list given the head
def printList(head):
    if head == None:
        print("None")
    else:
        print(head.val, end="")
        current = head.next
        while current != None:
            print(" -> " + str(current.val), end="")
            current = current.next
        print()

if __name__ == "__main__":
    # Test case 1
    list1 = ListNode(1)
    list1.next = ListNode(5)
    list1.next.next = ListNode(7)
    list2 = ListNode(2)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    print(printList(Solution().mergeTwoLists(list1, list2)))
