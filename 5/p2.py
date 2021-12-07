"""did this in a notebook so idk if it will run. who cares it's saturday baby"""

from functools import reduce
from collections import Counter

def get_diagonal_points(start_x, start_y, end_x, end_y):
    if start_x > end_x:
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

    result = []
    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
        result += [(i, j)]
    result.append((end_x, end_y))  # add end point
    return result


def get_points(l, r, diag):
    x, y = l
    _x, _y = r
    
    x_min = min(x, _x)
    x_max = max(x, _x) 
    
    y_min = min(y, _y)
    y_max = max(y, _y)
    
    if (x != _x) and (y != _y):
        print("word")
        return get_diagonal_points(x, y, _x, _y)
    
    possible_points = []
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            possible_points += [(i, j)]
    return possible_points

ahh = Counter(reduce(lambda x, y: x + y, [list(_) for _ in intervals]))
print(len([_ for k, v in ahh.items() if v > 1]))
