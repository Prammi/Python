matrix = [
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0]
]

visited = set()  # To track visited positions
path = []  # To store the route

def findPath(i, j):
    if matrix[i][j] == 0 and (i, j) not in visited:
        visited.add((i, j))
        path.append((i, j))  # Add current cell to path

        # Explore all directions: top, bottom, right, left
        if i > 0:  # Top
            findPath(i - 1, j)
        if i < len(matrix) - 1:  # Bottom
            findPath(i + 1, j)
        if j < len(matrix[0]) - 1:  # Right
            findPath(i, j + 1)
        if j > 0:  # Left
            findPath(i, j - 1)

findPath(0, 0)  # Start at (0,0)

print("Path covering all 0s:", path)
