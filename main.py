

import tkinter as tk


class SnakeGame(tk.Canvas):
    ''' game settings '''

    def __init__(self):
        super().__init__(width = 600, height = 620, background = 'salmon1', highlightthickness = 0 )


class SnakeApp:
    ''' main class '''

    def run(self):
        root = tk.Tk()
        root.title('#StayAtHome')
        root.resizable(False, False)

        game = SnakeGame()
        game.pack()

        root.mainloop()

if __name__ == '__main__':
    SnakeApp().run()
