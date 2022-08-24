"""
Algorithm - Merge Sort on Linked List
Reference:
    - https://www.youtube.com/watch?v=8hly31xKli0
    - https://teamtreehouse.com/library/introduction-to-data-structures/merge-sort-and-linked-lists/implementing-merge-sort-on-linked-lists
Last edited: 2022-08-24
"""
# This file needs the LinkedList class from another file
from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sort a linked list in ascending order.
    Return a sorted linked list

    Steps:
    1. Recursively divide the linked list into sublists containing a single node
    2. Repeatedly merge the sublists to produce sorted sublists until one remains

    Take O(n log n) time
    """
    # Stopping condition
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into two sublists.
    Return two sublists - left and right

    Take O(log n) time
    """
    if (linked_list is None) or (linked_list.head is None):
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        # Find the node after which the linked list is split into two
        # E.g. if size = 5, then mid = 2 and mid-1 = 1
        # so the tail of left_half is the node at index 1
        # and the head of right_half is the node at index 2
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.search_index(mid-1)
        
        left_half = linked_list

        # Right_half is a new LinkedList instance that is empty
        right_half = LinkedList()

        # The node after mid_node becomes the head of right_half, and
        # the node(s) following that node become a part of right_half
        right_half.head = mid_node.next_node

        # Mid_node becomes the tail of left_half, and
        # the connection between the two portions of linked list is broken
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merge two linked lists, sorting by data in nodes
    Return a new, merged list

    Take O(n) time
    """
    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    # Add a fake head that will be discarded later
    merged.prepend(0)
    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until reaching the tail node of either
    while left_head or right_head:
        # If head of left is None, the tail is passed; so add nodes of right to merged
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        
        # If head of right is None, the tail is passed; so add nodes of left to merged
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node

        # Not at head or tail node; so obtain and compare node data
        else:
            left_data = left_head.data
            right_data = right_head.data

            # If data on left is smaller than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to the next node
                left_head = left_head.next_node
            # If data on left is larger than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to the next node
                right_head = right_head.next_node

        # Move current to next node
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged