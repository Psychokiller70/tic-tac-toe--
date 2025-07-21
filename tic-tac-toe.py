import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.build_gui()

    def build_gui(self):
        label = tk.Label(self.root, text="Tic Tac Toe", font=('Poppins black', 24))
        label.grid(row=0, column=0, columnspan=3, pady=10)
        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.root, text="", width=8, height=4,
                                font=('Poppins', 20),
                                bg='white',               # Default background
                                fg='black',
                                activebackground='#C5C6C6',
                                command=lambda r=r, c=c: self.click(r, c))
                btn.grid(row=r+1, column=c, padx=2, pady=2)
                self.buttons[r][c] = btn
        reset = tk.Button(self.root, text="Restart", command=self.reset)
        reset.grid(row=4, column=0, columnspan=3, pady=10)

    def click(self, r, c):
        btn = self.buttons[r][c]
        if not self.board[r][c]:
            self.board[r][c] = self.current_player
            btn['text'] = self.current_player
            if self.current_player == "X":
                btn.config(fg='#57B14C', bg='black')  # 'X' के लिए रंग
            else:
                btn.config(fg='yellow', bg='black')  # 'O' के लिए रंग
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_all()
            elif all(self.board[i][j] for i in range(3) for j in range(3)):
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, p):
        b = self.board
        return any(all(b[r][c] == p for c in range(3)) for r in range(3)) or \
               any(all(b[r][c] == p for r in range(3)) for c in range(3)) or \
               all(b[i][i] == p for i in range(3)) or \
               all(b[i][2-i] == p for i in range(3))

    def disable_all(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

    def reset(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state=tk.NORMAL, bg='white', fg='black')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
