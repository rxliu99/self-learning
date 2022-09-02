"""
Algorithm - Selection Sort
Reference:
    - https://www.youtube.com/watch?v=8hly31xKli0
    - https://teamtreehouse.com/library/algorithms-sorting-and-searching/code-for-selection-sort
Last edited: 2022-09-02
"""

# An algorithm that takes a long time to run when the input is a large dataset
# So only useful for a short list of values
def selection_sort(values):
    """
    Loop x times, where x equals the length of the list of values
    Within each loop, locate the minimum value, remove it from the list,
        and add it to the sorted list
    Return the sorted list after the loops
    """
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    """
    Return in index of the minimum value in the list of values
    """
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index
