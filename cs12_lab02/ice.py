EMPTY = '.'
 
 
def ice_puzzle(grid: str, commands: list[str], start: tuple[int,int], facing: str) -> None:
    grid = grid.split('\n')                      # list[str] allows grid[row][col] indexing:
    r, c = start                                     # ['x..x......xx',
                                                     #  'x...........',
    for command in commands:                         #  '........x.xx',
        if command in {'F', 'B'}:                    #  '..x...x...xx',]
            deltas = {
                'up': (-1, 0),
                'down': (+1, 0),
                'left': (0, -1),
                'right': (0, +1),
            }
 
            dr, dc = deltas[facing]                  # Deltas for row (dr) and col (dc)
 
            if command == 'B':                       # Backward has opposite delta of forward
                dr *= -1
                dc *= -1
 
            next_r = r + dr
            next_c = c + dc
 
            while 0 <= next_r and next_r < len(grid) and \
                0 <= next_c and grid and next_c < len(grid[0]) and \
                grid[next_r][next_c] == EMPTY:
 
                r = next_r                           # Slide while possible
                c = next_c
                next_r = r + dr
                next_c = c + dc
 
            r = next_r
            c = next_c
 
        elif command == 'L':
            ccw_ordered_facing = ['up', 'left', 'down', 'right']
            idx = ccw_ordered_facing.index(facing)
            facing = ccw_ordered_facing[(idx + 1) % len(ccw_ordered_facing)]
 
        elif command == 'R':
            cw_ordered_facing = ['up', 'right', 'down', 'left']
            idx = ccw_ordered_facing.index(facing)
            facing = ccw_ordered_facing[(idx + 1) % len(ccw_ordered_facing)]
 
    return ((r, c), facing)