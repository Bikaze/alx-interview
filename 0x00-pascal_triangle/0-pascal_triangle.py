#!/usr/bin/python3
"""
This script implements the pascal_triangle function
---> pascal_triangle(n)
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    Explanation:
        The algorithm generates Pascal's triangle by iterating over each row (k) up to the given number of rows (n).
        For each row, a new list called `triangle` is created.
        Within each row, the algorithm iterates over each element (i) up to the current row number (k+1).
        If the element is the first element (i == 0), it appends 1 to the `triangle` list.
        Otherwise, it calculates the value of the current element by summing the previous row's element at index (i-1)
        (stored in `nbr1`) and the previous row's element at index (i) (stored in `nbr2`).
        If the previous row does not exist or the indices are out of range, the value is considered as 0.
        The calculated value is then appended to the `triangle` list.
        Finally, the `triangle` list is appended to the `triangles` list, which represents the entire Pascal's triangle.
        The `triangles` list is returned as the result.

    """

    if n <= 0:
        return []
    triangles = []
    for k in range(n):
        triangle = []
        for i in range(k+1):
            if i == 0:
                triangle.append(1)
            else:
                prev_l = triangles[-1] if len(triangles) > 0 else []
                nbr1 = prev_l[i-1] if (i-1) in range(len(prev_l)) else 0
                nbr2 = prev_l[i] if (i) in range(len(prev_l)) else 0
                triangle.append(nbr1 + nbr2)
        triangles.append(triangle)
    return triangles
