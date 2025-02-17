import random

MAZE_WIDTH = 21
MAZE_HEIGHT = 11

WALL = '#'
SPACE = ' '

def generate_maze(width, height):
    maze = [[WALL for x in range(width)] for y in range(height)]
    stack = [(0, 0)]
    
    while stack:
        (x, y) = stack[-1]
        maze[y][x] = SPACE
        
        neighbors = [(x-2, y) if x > 1 and maze[y][x-2] == WALL else None,
                      (x+2, y) if x < width-2 and maze[y][x+2] == WALL else None,
                      (x, y-2) if y > 1 and maze[y-2][x] == WALL else None,
                      (x, y+2) if y < height-2 and maze[y+2][x] == WALL else None]
        neighbors = [neighbor for neighbor in neighbors if neighbor]
        
        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[ny][nx] = SPACE
            maze[y+(ny-y)//2][x+(nx-x)//2] = SPACE
            stack.append((nx, ny))
        else:
            stack.pop()
    
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def dfs_solve(maze, start, end):
    stack = [start]
    visited = set()
    
    while stack:
        x, y = stack.pop()
        if (x, y) == end:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        neighbors = [(x-1, y) if x > 0 and maze[y][x-1] == SPACE else None,
                      (x+1, y) if x < len(maze[0])-1 and maze[y][x+1] == SPACE else None,
                      (x, y-1) if y > 0 and maze[y-1][x] == SPACE else None,
                      (x, y+1) if y < len(maze)-1 and maze[y+1][x] == SPACE else None]
        neighbors = [neighbor for neighbor in neighbors if neighbor]
        stack.extend(neighbors)
    
    return False

def bfs_solve(maze, start, end):
    queue = [start]
    visited = set()
    
    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        neighbors = [(x-1, y) if x > 0 and maze[y][x-1] == SPACE else None,
                      (x+1, y) if x < len(maze[0])-1 and maze[y][x+1] == SPACE else None,
                      (x, y-1) if y > 0 and maze[y-1][x] == SPACE else None,
                      (x, y+1) if y < len(maze)-1 and maze[y+1][x] == SPACE else None]
        neighbors = [neighbor for neighbor in neighbors if neighbor]
        queue.extend(neighbors)
    
    return False

maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
print("Maze:")
print_maze(maze)

start = (1, 1)
end = (MAZE_WIDTH-2, MAZE_HEIGHT-2)

print(dfs_solve(maze, start, end))
print(bfs_solve(maze, start, end))
```
