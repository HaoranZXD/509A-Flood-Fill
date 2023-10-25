board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board, old, new, x, y):
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]) or input_board[x][y] != old:
        return input_board
    
    # Replace the old value with the new value
    input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
    
    # Recursively call flood_fill for neighboring cells
    flood_fill(input_board, old, new, x-1, y)  # Up
    flood_fill(input_board, old, new, x+1, y)  # Down
    flood_fill(input_board, old, new, x, y-1)  # Left
    flood_fill(input_board, old, new, x, y+1)  # Right
    
    return input_board

    
 


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)

for a in modified_board:
    print(a)

# Expected output:
#~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~##########~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#####~~
#~~~~###............#~~
#~~~~#............###~~
#~~~~##############~~~~