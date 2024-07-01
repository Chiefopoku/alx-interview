def pascal_triangle(n):
    if n <= 0:
        return []  # Returns an empty list if n is less than or equal to 0
    
    # Start with the first row
    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        # Calculate the elements of the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is also always 1
        triangle.append(row)
    
    return triangle
