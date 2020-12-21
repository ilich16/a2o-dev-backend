from typing import Dict, List

class Position:
    """
    A class used to represent a position on a board.

    ...

    Attributes
    ----------
    row : int
        the row of the board
    column : int
        the column of the board

    """
    def __init__(self, row: int, column: int):
        """
        Parameters
        ----------
        row : int
            the row of the board
        column : int
            the column of the board

        """
        self.row = row
        self.column = column

    def __str__(self) -> str:
        return f'Row: {self.row}, Column: {self.column}'
  
    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
    
        return self.row == other.row and self.column == other.column

class SecondProblem:
    """
    A class used to represent the second problem in the project

    ...

    Attributes
    ----------
    user_input : str
        the user input text for the second problem

    Methods
    -------
    get_answer() -> int
        Get the answer of the problem

    """

    def __init__(self, user_input: str):
        """
        Parameters
        ----------
        user_input : str
            the user input text of the problem

        """
        self.user_input = user_input

    def get_answer(self) -> int:
        """
        Get the answer for the second problem

        Returns
        -------
        int
            an int that represents the number of moves for the queen

        """
        # Get all lines from the user input text
        lines = self.user_input.split('\n')
        # Get the first line
        first_line = lines[0]
        # Get the board size from the first line
        board_size = first_line.split(' ')[0]
        # Get the number of obstacles from the first line
        number_of_obstacles = first_line.split(' ')[1]
        # Get the second line
        second_line = lines[1]
        # Get the row number of the queen's position from the second line
        row_queen = second_line.split(' ')[0]
        # Get the column number of the queen's position from the second line
        column_queen = second_line.split(' ')[1]
        obstacles = []
        # Iterate over the lines except for the first two lines
        for line in lines[2:]:
            # Save position of the obstacles in an array
            row = int(line.split(' ')[0])
            column = int(line.split(' ')[1])
            obstacle = [row, column]
            obstacles.append(obstacle)
        
        # Call the function queens_attack for get the result
        return queens_attack(int(board_size), int(number_of_obstacles), int(row_queen), int(column_queen), obstacles)

def get_possible_moves(board_size: int, queen_position: Position) -> Dict[str, List[Position]]:
    """
    Get the possible moves that one queen can has on a board

    Parameters
    ----------
    board_size : int
        the size of the board
    queen_position : Position
        the position of the queen on the board

    Returns
    -------
    Dict[str, List[Position]]
        a dictionary where each data value is the name of the direction
        with its possible positions

    """
    possible_moves: Dict[str, list[Position]] = {}

    # Get the possible positions to move to based on each direction
    # following a clock direction

    # Top direction
    top_direction = []
    for i in range(queen_position.row + 1, board_size + 1):
        position = Position(i, queen_position.column)
        top_direction.append(position)
    possible_moves["top_direction"] = top_direction

    # First diagonal
    first_diagonal = []
    j = 1
    while True:
        position = Position(queen_position.row + j, queen_position.column + j)
        if position.row > board_size or position.column > board_size:
            break
        j += 1
        first_diagonal.append(position)
    possible_moves["first_diagonal"] = first_diagonal

    # Right direction
    right_direction = []
    for i in range(queen_position.column + 1, board_size + 1):
        position = Position(queen_position.row, i)
        right_direction.append(position)
    possible_moves["right_direction"] = right_direction

    # Second diagonal
    second_diagonal = []
    j = 1
    while True:
        position = Position(queen_position.row - j, queen_position.column + j)
        if position.row < 1 or position.column > board_size:
            break
        j += 1
        second_diagonal.append(position)
    possible_moves["second_diagonal"] = second_diagonal

    # Bottom direction
    bottom_direction = []
    for i in range(1, queen_position.row):
        position = Position(queen_position.row - i, queen_position.column)
        bottom_direction.append(position)
    possible_moves["bottom_direction"] = bottom_direction

    # Third diagonal
    third_diagonal = []
    j = 1
    while True:
        position = Position(queen_position.row - j, queen_position.column - j)
        if position.row < 1 or position.column < 1:
            break
        j += 1
        third_diagonal.append(position)
    possible_moves["third_diagonal"] = third_diagonal

    # Left direction
    left_direction = []
    for i in range(1, queen_position.column):
        position = Position(queen_position.row, queen_position.column - i)
        left_direction.append(position)
    possible_moves["left_direction"] = left_direction

    # Fourth diagonal
    fourth_diagonal = []
    j = 1
    while True:
        position = Position(queen_position.row + j, queen_position.column - j)
        if position.row > board_size or position.column < 1:
            break
        j += 1
        fourth_diagonal.append(position)
    possible_moves["fourth_diagonal"] = fourth_diagonal

    return possible_moves

def get_obstacles_positions(obstacles: []) -> List[Position]:
    """
    Get the positions of the obstacles from a two-dimensional array

    Parameters
    ----------
    obstacles : []
        obstacles in a two-dimensional array

    Returns
    -------
    List[Position]
        a list with all positions of the obstacles

    """
    obstacles_positions: List[Position] = []
    # Iterate over two-dimensional array
    for obstacle in obstacles:
        # Create a position object to append to a list
        position = Position(obstacle[0], obstacle[1])
        obstacles_positions.append(position)
    
    return obstacles_positions

def queens_attack(n: int, k: int, rq: int, cq: int, obstacles: []) -> int:
    """
    Get the number of squares the queen can attack

    Parameters
    ----------
    n : int
        the number of rows and columns in the board
    k : int
        the number of obstacles on the board
    rq : int
        the row number of the queen's position
    cq : int
        the column number of the queen's position
    obstacles : []
        a two-dimensional array of integers where each element is an array
        of integers, the row and column of an obstacle

    Returns
    -------
    int
        return an int that describes the number of squares the queen can attack

    """
    obstacles_positions = get_obstacles_positions(obstacles)
    queen_position = Position(rq, cq)
    possible_moves = get_possible_moves(n, queen_position)
    quantity_moves = 0
    # Iterate over all possible moves
    for _, moves in possible_moves.items():
        for position in moves:
            # Check if a obstacle blocks a move
            if position in obstacles_positions:
                break
            quantity_moves += 1

    return quantity_moves
