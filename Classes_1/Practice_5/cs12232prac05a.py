from typing import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def is_axis_aligned(polygon:Sequence[Point])-> bool:
    list_of_points:list[Point]=[]
    if len(polygon)!=4:
        raise ValueError
    for i in polygon:
        if i not in list_of_points:
            list_of_points.append(i)
        else:
            raise ValueError
    x_values = [point.x for point in polygon]
    y_values = [point.y for point in polygon]
    for i in range(3):
        if x_values[i]!=x_values[i+1] and y_values[i]!=y_values[i+1]:
            return False
    return (len(set(x_values)) == 2) and (len(set(y_values)) == 2)

