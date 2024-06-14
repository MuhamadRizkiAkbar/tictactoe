def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return all(cell != " " for cell in board)

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"
    players = {"X": "Player 1", "O": "Player 2"}
    
    while True:
        print_board(board)
        try:
            move = int(input(f"{players[current_player]}, Tolong Masukan Langkah Anda (1-9 Menyamping): ")) - 1
            if move < 0 or move > 8:
                print("Perintah yang anda Masukan Salah, Tolong Masukkan Angka 1-9.")
                continue
        except ValueError:
            print("Perintah yang anda Masukan Salah, Tolong Masukkan Angka 1-9.")
            continue

        if board[move] == " ":
            board[move] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"{players[current_player]} Menang!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ini seri!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Perintah yang anda Masukan Salah, Kotak Sudah Terisi, Tolong Coba Lagi.")

if __name__ == "__main__":
    play_game()
