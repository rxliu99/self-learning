"""
Algorithm - Merge Sort
Reference:
    - https://www.youtube.com/watch?v=8hly31xKli0
    - https://teamtreehouse.com/library/introduction-to-data-structures/the-merge-sort-algorithm/merge-sort-implementations
Last edited: 2022-08-22
"""

def merge_sort(lst):
    """
    The body function of the algorithm
    Sort a list in ascending order, and return the sorted list

    Steps:
    1. Divide: Find the midpoint of the list and divide into sublists
    2. Conquer: Recursively sort the sublists created in step 1
    3. Combine: Merge the sorted sublists created in step 2

    Take overall O(n log n) time
    """
    #stopping condition
    if len(lst) <= 1:
        return lst

    left_half, right_half = split(lst)
    
    #recursive portion of algorithm
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(lst):
    """
    Divide the unsorted list at midpoint into two sublists
    Return two sublists - left and right
    
    Take overall O(log n) time
    """
    mid = len(lst) // 2
    left = lst[:mid]  #the upper bound of slicing is exclusive
    right = lst[mid:]

    return left, right

def merge(left, right):
    """
    Merge two lists while sorting them in the process
    Return a new merged list

    Take overall O(n) time
    """
    sorted_lst = []
    i = 0
    j = 0

    #can complete the task by itself if the two sublists have the same length
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1

    #goes into action only if len(left) > len(right)
    while i < len(left):
        sorted_lst.append(left[i])
        i += 1
    
    #goes into action only if len(left) < len(right)
    while j < len(right):
        sorted_lst.append(right[j])
        j += 1
    
    return sorted_lst

def verify_sorted(sorted_lst):
    """
    Check if the list passed in is sorted in ascending order
    Return True if the list is sorted correctly
    """
    n = len(sorted_lst)

    if (n == 0) or (n == 1):
        return True
    
    return sorted_lst[0] < sorted_lst[1] and verify_sorted(sorted_lst[1:])
