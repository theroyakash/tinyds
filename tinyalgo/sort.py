"""
For more rigorous implementation see AKDSFramework Module

This implementation is mainly for quick implementation purpose in an interview setting.
"""

def merge_sort(iterable):
    if len(iterable) == 1 or iterable == []:
        return iterable

    mid = len(iterable) // 2
    left, right = iterable[:mid], iterable[mid:]

    # Recursive call on the left side and the right side
    merge_sort(left, right)


    # Implementation on going
    raise(NotImplementedError)