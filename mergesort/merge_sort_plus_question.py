# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

import math

# trying to modify to not have two
# indices.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def split(head, n):
            node = head
            for i in range(n):
                node = node.next
            return node

        def merge_sort(head, length):

            if length == 1:
                # trivial case the list is already sorted
                return head

            else:

                # split the list into two parts
                n = int(length // 2)

                part1 = head
                part2 = split(part1, n)

                # sort each part separatly
                part1 = merge_sort(part1, n)
                part2 = merge_sort(part2, length - n)

                # merge the two part
                left_pointer = part1  # pointer to left part
                right_pointer = part2  # pointer to right part

                # count the number of steps moved so far over left part
                left = 0
                # count the number of steps moved so far over right part
                right = 0

                if part1.val > part2.val:
                    sorted_list = part2
                    right_pointer = part2.next
                    right += 1
                else:
                    sorted_list = part1
                    left_pointer = part1.next
                    left += 1

                sorted_head = sorted_list

                while left + right < length:

                    if right == length - n:
                        sorted_list.next = left_pointer
                        left_pointer = left_pointer.next
                        left += 1
                        sorted_list = sorted_list.next
                        continue

                    if left == n:
                        sorted_list.next = right_pointer
                        right_pointer = right_pointer.next
                        right += 1
                        sorted_list = sorted_list.next
                        continue

                    if left_pointer.val > right_pointer.val:
                        sorted_list.next = right_pointer
                        right_pointer = right_pointer.next
                        right += 1
                    else:
                        sorted_list.next = left_pointer
                        left_pointer = left_pointer.next
                        left += 1

                    sorted_list = sorted_list.next

                return sorted_head

        node = head
        length = 1

        while node.next:
            node = node.next
            length += 1

        sorted_head = merge_sort(head, length)

        return sorted_head


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)


a = Solution()
head = a.sortList(head)

print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)
