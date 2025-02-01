import copy

def calc_cartesian_product(lsts):
    points = [[]]

    for lst in lsts:
        points_copy = copy.deepcopy(points)
        extended_points = []
        for i in range(len(points_copy)):
            for val in lst:
                extended_point = copy.deepcopy(points_copy[i])
                extended_point.append(val)
                extended_points.append(extended_point)
        points = extended_points

    return points
