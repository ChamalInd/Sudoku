import random
import copy

# boiler plate of board
full_board = [
    [['1x1x1', '1x1x2', '1x1x3'], ['1x2x1', '1x2x2', '1x2x3'], ['1x3x1', '1x3x2', '1x3x3']],
    [['2x1x1', '2x1x2', '2x1x3'], ['2x2x1', '2x2x2', '2x2x3'], ['2x3x1', '2x3x2', '2x3x3']],
    [['3x1x1', '3x1x2', '3x1x3'], ['3x2x1', '3x2x2', '3x2x3'], ['3x3x1', '3x3x2', '3x3x3']],
    [['4x1x1', '4x1x2', '4x1x3'], ['4x2x1', '4x2x2', '4x2x3'], ['4x3x1', '4x3x2', '4x3x3']],
    [['5x1x1', '5x1x2', '5x1x3'], ['5x2x1', '5x2x2', '5x2x3'], ['5x3x1', '5x3x2', '5x3x3']],
    [['6x1x1', '6x1x2', '6x1x3'], ['6x2x1', '6x2x2', '6x2x3'], ['6x3x1', '6x3x2', '6x3x3']],
    [['7x1x1', '7x1x2', '7x1x3'], ['7x2x1', '7x2x2', '7x2x3'], ['7x3x1', '7x3x2', '7x3x3']],
    [['8x1x1', '8x1x2', '8x1x3'], ['8x2x1', '8x2x2', '8x2x3'], ['8x3x1', '8x3x2', '8x3x3']],
    [['9x1x1', '9x1x2', '9x1x3'], ['9x2x1', '9x2x2', '9x2x3'], ['9x3x1', '9x3x2', '9x3x3']], 
]

game_board = None

# indexes of diagonals
index_top_left = [
    [0, 0, 0], [0, 0, 1], [0, 0, 2],
    [1, 0, 0], [1, 0, 1], [1, 0, 2],
    [2, 0, 0], [2, 0, 1], [2, 0, 2]
]

index_middle = [
    [3, 1, 0], [3, 1, 1], [3, 1, 2],
    [4, 1, 0], [4, 1, 1], [4, 1, 2],
    [5, 1, 0], [5, 1, 1], [5, 1, 2]
]

index_bottom_right = [
    [6, 2, 0], [6, 2, 1], [6, 2, 2],
    [7, 2, 0], [7, 2, 1], [7, 2, 2],
    [8, 2, 0], [8, 2, 1], [8, 2, 2]
]

def fill_small_boxes(board, index_arr):
    num_list = []
    for i in range(len(index_arr)):
        while True:
            number = random.randint(1, 9)
            if number not in num_list:
                num_list.append(number)
                break
        board[index_arr[i][0]][index_arr[i][1]][index_arr[i][2]] = number


def is_safe(board, row, sec, col, number):
    # check horizontally
    for i in range(3):
        for j in range(3):
            if board[row][i][j] == number:
                return False

    # check vertically   
    for i in range(9):
        if board[i][sec][col] == number:
            return False

    # check inside the section    
    row_start = (row // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(3):
            if board[i][sec][j] == number:
                return False
            
    return True
        

def fill_empty_spaces(board):
    for row in range(9):
        for sec in range(3):
            for col in range(3):
                if not isinstance(board[row][sec][col], int):
                    num_list = list(range(1, 10))
                    random.shuffle(num_list)

                    for number in num_list:
                        if is_safe(full_board, row, sec, col, number):
                            board[row][sec][col] = number

                            if fill_empty_spaces(board):
                                return True
                            
                            board[row][sec][col] = None
                    return False 
    return True


def generate_game_board(board, difficulty):
    global game_board
    game_board = copy.deepcopy(board)

    difficulty_levels = [
        random.randint(36, 46), random.randint(30, 35),
        random.randint(24, 29), random.randint(17, 23)
    ]

    empty_spaces = 81 - difficulty_levels[difficulty]

    for _ in range(empty_spaces):
        while True:
            row = random.randint(0, 8)
            sec = random.randint(0, 2)
            col = random.randint(0, 2)

            if isinstance(game_board[row][sec][col], int):
                game_board[row][sec][col] = ' '
                break
    return game_board


def clear_board(board):
    for row in range(9):
        for sec in range(3):
            for col in range(3):
                board[row][sec][col] = f'{row + 1}x{sec + 1}x{col + 1}'

    return board


def print_board(board):
    for row in range(9):
        for sec in range(3):
            for col in range(3):
                print(board[row][sec][col], end=' ')
            print(' ', end='')
        print()
        if (row + 1) % 3 == 0 and row != 8:
            print()


def generate(difficulty):
    global index_bottom_right, index_middle, index_bottom_right, full_board

    # clear previously generated board
    full_board = clear_board(full_board)

    # filling diagonals
    fill_small_boxes(full_board, index_top_left)
    fill_small_boxes(full_board, index_middle)
    fill_small_boxes(full_board, index_bottom_right)

    # filling empty spaces
    fill_empty_spaces(full_board)

    # generating game board
    game_board = generate_game_board(full_board, difficulty)

    return full_board, game_board

