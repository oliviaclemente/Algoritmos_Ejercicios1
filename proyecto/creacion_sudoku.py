class SudokuBoard:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]  # Inicializar un tablero vacío

    def load_board(self, board):
        """
        Cargar un tablero de Sudoku desde una matriz 9x9.
        """
        if len(board) != 9 or any(len(row) != 9 for row in board):
            raise ValueError("El tablero debe ser una matriz 9x9.")
        self.board = board

    def print_board(self):
        """
        Imprimir el tablero de Sudoku.
        """
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j], end=" ")
            print()

# Ejemplo de uso:
# Crear un nuevo tablero de Sudoku
sudoku = SudokuBoard()

# Cargar un tablero de ejemplo
example_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
sudoku.load_board(example_board)

# Imprimir el tablero de Sudoku cargado
sudoku.print_board()

