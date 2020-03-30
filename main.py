

import tkinter as tk
from PIL import Image, ImageTk


# define constants
MOVE_INCREMENT = 20
MOVES_PER_SECOND = 15
GAME_SPEED = 1000 // MOVES_PER_SECOND

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
        self.rectangle()

        self.after(75, self.perform_actions)


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
            self.create_image(x_position, y_position, image = self.snake_body, tag = 'snake')


    def create_food(self):
        self.create_image(
                self.food_position[0], self.food_position[1], image = self.food, tag = 'food'
                )


    def create_score(self):
        self.create_text(45, 12, text = f'Score: {self.score}', tag = 'socre', fill = '#000', font=('Helvetica', 16) )


    def rectangle(self):
      self. create_rectangle(7, 27, 593, 613, outline = '#525d69')


    def snake_move(self):
        head_x_position, head_y_position = self.snake_positions[0]
        new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag('snake'), self.snake_positions):
            self.coords(segment, position)
    

    def perform_actions(self):
        self.snake_move()
        self.after(GAME_SPEED, self.perform_actions)
    

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
