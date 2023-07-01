class PegSolitaire:
    def __init__(self, board):
        self.board_type = board
        self.board = self.create_board(board)

    def create_board(self, board):

        array = []

        if(board == "cross"):
            
            array = [
                [0,0,0,1,1,1,0,0,0],
                [0,0,0,1,1,1,0,0,0],
                [1,1,1,1,1,1,1,1,1],
                [1,1,1,1,2,1,1,1,1],
                [1,1,1,1,1,1,1,1,1],
                [0,0,0,1,1,1,0,0,0],
                [0,0,0,1,1,1,0,0,0],

            ]

        if(board == "circle"):

            array = [

                [0,2,1,1,2,0],
                [2,1,1,1,1,2],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [2,1,1,1,1,2],
                [0,2,1,1,2,0],

            ]

        if(board == "triangle"):

            array = [

                [0,0,0,2,1,2,0,0,0],
                [0,0,2,1,1,1,2,0,0],
                [0,2,1,1,2,1,1,2,0],
                [2,1,1,1,1,1,1,1,2]
            ]
        
        if(board == "t"):

            array = [

                [2,2,2,2,2],
                [2,1,1,1,2],
                [2,2,1,2,2],
                [2,2,1,2,2],
                [2,2,2,2,2]
            ]
        
        return array
            
    def board_display(self):
        print("  ", end="")
        for col in range(len(self.board[0])):
            print(col+1, end=" ")
        print()

        # Display row numbers and board cells
        for row in range(len(self.board)):
            # Display row number
            print(row+1, end=" ")

            for cell in self.board[row]:
                if cell == 1:
                    print("X", end=" ")
                elif cell == 2:
                    print("-", end=" ")
                else:
                    print(" ", end=" ")

            print()
    
    def valid_move_check(self, startr, startc, endr, endc):
        if(self.board[startr][startc] != 1):
            return False
        
        if(self.board[endr][endc] != 2):
            return False
        
        if(startr == endr and abs(startc - endc) == 2):
            midc = (startc + endc) // 2
            return self.board[startr][midc] == 1
        
        elif(startc ==  endc and abs(startr - endr) == 2):
            midr = (startr + endr) // 2
            return self.board[midr][startc] == 1
        
        else:
            return False
    
    def perform_move(self, startr, startc, endr, endc):
        if(self.valid_move_check(startr, startc, endr, endc)):
            self.board[startr][startc] = 2
            self.board[endr][endc] = 1
            self.board[(startr+endr)//2][(startc+endc)//2] = 2
        
        else:
            print("Invalid Move!")

    def valid_moves(self):
        rows = len(self.board)
        cols = len(self.board[0])
    
        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] == 1:
                    # Check horizontal moves
                    if col >= 2 and self.valid_move_check(row, col, row, col - 2):
                        return True
                    if col <= cols - 3 and self.valid_move_check(row, col, row, col + 2):
                        return True
                    # Check vertical moves
                    if row >= 2 and self.valid_move_check(row, col, row - 2, col):
                        return True
                    if row <= rows - 3 and self.valid_move_check(row, col, row + 2, col):
                        return True
        return False
    
    def num_of_pegs(self):
        sum = 0
        
        for row in self.board:
            for cell in row:
                if cell == 1:
                    sum = sum + 1
        
        return sum
    
    def start(self):
        self.board_display()
        while(self.valid_moves()):
            start_row = (int(input("Enter the starting row: ")))-1
            start_col = (int(input("Enter the starting column: ")))-1
            end_row = (int(input("Enter the ending row: ")))-1
            end_col = (int(input("Enter the ending column: ")))-1

            self.perform_move(start_row, start_col, end_row, end_col)
            self.board_display()

            if(self.num_of_pegs() == 1):
                print("You won!")
                break 
        
        else:
            print("Game Over!")
            print("You have run out of valid moves!")
            


repeat = True
while(repeat):
    print("Welcome to the Peg Solitaire Game!")
    print("============================")
    print()
    print("Board Types: ")
    print("Cross")
    print("Circle")
    print("Triangle")
    print("T")
    board_type = input("Enter the board type: ")
    board_type = board_type.lower()
    game = PegSolitaire(board_type)
    game.start()
    print("============================")
    print()

    repeat = input("Do you want to play again? (y/n): ")
    repeat = repeat.lower()
    if(repeat == "n"):
        repeat = False



    
