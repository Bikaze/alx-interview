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
