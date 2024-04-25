
from Stack import Stack

def maze_path_exists(maze, start_x, start_y):
    path_stack = Stack()
    path_stack.push([start_x, start_y])
    count = 1
    maze[start_x][start_y] = count
    path_found = False

    while not path_found and not path_stack.isEmpty():
        row, column = path_stack.peek()

        did_move = False
        moves = [(row - 1, column), (row, column - 1), (row + 1, column), (row, column + 1)]

        for r, c in moves:
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] in [' ', 'G']:
                if maze[r][c] == 'G':
                    path_found = True
                    did_move = True
                    break
                count += 1
                maze[r][c] = count
                path_stack.push([r, c])
                did_move = True
                break
       
        if did_move == False:
            path_stack.pop()

    return path_found 
