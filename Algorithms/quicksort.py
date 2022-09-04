"""
Algorithm - Quicksort
Reference:
    - https://www.youtube.com/watch?v=8hly31xKli0
    - https://teamtreehouse.com/library/algorithms-sorting-and-searching/code-for-quicksort
Last edited: 2022-09-03
"""

def quicksort(values):
    """
    Sort a list in ascending order, and return the sorted list

    Steps:
    1. Pick a pivot (here, the pivot is the first value of the list)
    2. Split the list into two sublists, sublist 1 with values less than or equal to the pivot,
       and sublist 2 with values greater than the pivot
    3. Repeat steps 1 and 2 with each of the sublists, until the length of 
       all of the sublists is zero (an empty list) or one
    4. The sublists are joined together with the pivot in the following order: 
       sublist 1, pivot, sublist 2
    5. Empty sublists are discarded in step 4
    6. The single sorted list is returned
    """
    # base case of the recursion
    if len(values) <= 1:
        return values
    
    # recursive case
    pivot = values[0]
    less_than_pivot = []
    greater_than_pivot = []
    
    for value in values:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)