def print_board(board):
    print("---------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell if cell != "" else " ", end=" ")
        print("|")
    print("---------")

def check_winner(board):
    # שורות
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    # עמודות
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    # אלכסונים
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

def board_full(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def play_game():
    board = [["" for _ in range(3)] for _ in range(3)]
    current = "X"
    while True:
        print_board(board)
        print(f"תור השחקן: {current}")
        try:
            move = input("הכנס שורה ועמודה (לדוג' 1 2): ").strip()
            row, col = map(int, move.split())
            row -= 1
            col -= 1
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != "":
                print("מהלך לא חוקי. נסה שוב.")
                continue
            board[row][col] = current
        except Exception:
            print("קלט לא חוקי. נסה שוב.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"השחקן {winner} ניצח!")
            break
        if board_full(board):
            print_board(board)
            print("תיקו!")
            break
        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    play_game()