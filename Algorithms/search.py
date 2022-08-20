"""
Algorithm - Linear and Binary Search
Reference:
    - https://www.youtube.com/watch?v=8hly31xKli0
    - https://teamtreehouse.com/library/introduction-to-algorithms/algorithms-in-code/linear-search-implementations
    - https://teamtreehouse.com/library/introduction-to-algorithms/algorithms-in-code/binary-search-implementations
Last edited: 2022-08-19
"""

### Linear Search ###
# When starting from one end of a list and check every element of the list
#   until the desired element is found.
# Useful when:
#   - the list is unsorted
#   - the list only need to be searched once
#   - the list is small
#   - the list contain elements that are not numbers

def linear_search(lst, target):
    """
    Linearly search if target exists in the list.

    Inputs:
        lst: a list of items
        target: the target

    Return: the index if target exists in the list, and -1 if it doesn't
    """
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1


### Binary Search ###
# Steps:
#   1. Begin with the mid element of the list
#   2. If the mid element is equal to the target, return the index
#   3. If the mid element is more than the target, narrow the list to the lower half
#   4. If the mid element is less than the target, narrow the list to the upper half
#   5. Repeat from step 1 until the target is matched or the list is empty
# Useful when:
#   - the list is sorted
#   - the list contains numeric elements

def iterative_binary_search(lst, target):
    """
    Binary-ly search if target exists in the list.

    Inputs:
        lst: a list of items
        target: the target

    Return: the index if target exists in the list, and -1 if it doesn't
    """
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last) // 2
        mid_val = lst[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            first = mid + 1
        else:
            last = mid - 1
    
    return -1

def recursive_binary_search(list, target, start=0, end=None):
    """
    Binary-ly search if target exists in the list, using a recursive function.

    Inputs:
        lst: a list of items
        target: the target
        start: index of the start of the list
        end: index of the end of the list

    Return: the index if target exists in the list, and -1 if it doesn't
    """
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)
