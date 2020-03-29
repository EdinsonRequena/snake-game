

import tkinter as tk
from PIL import Image, ImageTk

class SnakeGame(tk.Canvas):
    ''' game settings '''

    def __init__(self):
        super().__init__(width = 600, height = 620, background = 'salmon1', highlightthickness = 0 )

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)
        self.score = 0

        self.assets()
        self.create_snake()
        self.create_food()
        self.create_score()


    def assets(self):
        try:
            self.snake_png = Image.open('./assets/snake.png')
            self.snake_body = ImageTk.PhotoImage(self.snake_png)

            self.food_png = Image.open('./assets/food.png')
            self.food = ImageTk.PhotoImage(self.food_png)
        except IOError as error:
            root.destroy()
            raise


    def create_snake(self):
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image = self.snake_body, tag = 'test')


    def create_food(self):
        self.create_image(
                self.food_position[0], self.food_position[1], image = self.food, tag = 'test 2'
                )


    def create_score(self):
        self.create_text(45, 12, text = f'Score: {self.score}', tag = 'socre', fill = '#000', font=('Helvetica', 16) )

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
