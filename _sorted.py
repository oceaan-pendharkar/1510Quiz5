def _sorted(list_of_integers):
    """
    Determine if a list of integers is sorted in non-decreasing order.

    :param list_of_integers: a list containing only integers, may be empty
    :precondition: list_of_integers must either be empty or contain only integers
    :postcondition: determines whether a list of integers is sorted or not
    :return: True if the list is sorted, else False
    >>> _sorted([1, 2, 3])
    True
    >>> _sorted([99, 5, 78])
    False
    """
    if list_of_integers and sorted(list_of_integers) == list_of_integers:
        return True
    return False
