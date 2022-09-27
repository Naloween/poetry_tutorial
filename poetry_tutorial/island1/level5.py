
"""level5
"""

def most_frequent(data):
    """calculate the most frequent element appearing in data

    Args:
        data (list): the list of element to get the most frequent element

    Returns:
        any: the element the most frequent in data
    """
    return max(set(data), key=data.count)
