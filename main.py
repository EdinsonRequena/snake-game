

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
        self.direction = 'Right'
        self.bind_all('<Key>', self.on_key_press)

        self.assets()
        self.create_snake()
        self.create_food()
        self.create_score()
        self.rectangle()

        self.after(GAME_SPEED, self.perform_actions)


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
        
        if self.direction == 'Left':
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == 'Right':
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == 'Down':
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == 'Up':
            new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag('snake'), self.snake_positions):
            self.coords(segment, position)
    

    def perform_actions(self):
        if self.collisions():
            return

        self.eat_food()
        self.snake_move()
        self.after(GAME_SPEED, self.perform_actions)


    def collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]

        return(
            head_x_position in (0, 600)
            or head_y_position in (20, 620)
            or (head_x_position, head_y_position) in self.snake_positions[1:]
        )


    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction


    def eat_food(self):
        if self.snake_positions[0] == self.food_position:
            self.score =+ 1
            self.snake_positions.append(self.snake_positions[-1])

            self.create_image(*self.snake_positions[-1], image = self.snake_body, tag = 'snake')

            score = self.find_withtag('score')
            self.itemconfigure(score, text = f'Score: {self.score}')


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
