board = [[" "]*3 for _ in range(3)]
for turn in range(9):
    [print(" | ".join(row)) for row in board]; r, c = map(int, input(f"Joueur {'XO'[turn%2]}, ligne et colonne : ").split()); board[r][c] = "XO"[turn%2] if board[r][c] == " " else board[r][c]
    if any(all(board[i][j] == "XO"[turn%2] for j in range(3)) or all(board[j][i] == "XO"[turn%2] for j in range(3)) for i in range(3)) or all(board[i][i] == "XO"[turn%2] for i in range(3)) or all(board[i][2-i] == "XO"[turn%2] for i in range(3)): print(f"Joueur {'XO'[turn%2]} gagne !"); exit()
print("Match nul !")
