points = [ (2, 3),
 (-1, 4),
 (5, -6),
 (0, 7),
 (-3, -2)
 ]
 
def two_positive_points(points):
    first_number,second_number = points
    return not (first_number > 0 and second_number > 0)
        
        
non_positive_points = list( filter(two_positive_points,points))

print(non_positive_points)


    
