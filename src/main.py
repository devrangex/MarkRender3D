import tkinter as tk
from renderer.dd.line2 import Line2
from renderer.dd.vector2 import Vector2
from renderer.dd.grid2 import Grid2

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 400
        self.height = 400
        self.canvas = tk.Canvas(self, bg="#aaaaff", width=self.width, height=self.height)

        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        # self.paddle = Paddle(self.canvas, self.width / 2, 326)
        # self.items[self.paddle.item] = self.paddle

        # for x in range(5, self.width - 5, 75):
        #     self.add_brick(x + 37.5, 50, 3)
        #     self.add_brick(x + 37.5, 70, 2)
        #     self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        # self.canvas.bind("<Left>",
        #                  lambda _: self.paddle.move(-10))
        # self.canvas.bind("<Right>",
        #                  lambda _: self.paddle.move(10))
        
        #self.line = Line2(self.canvas, Vector2(0, 0), Vector2(self.width, self.height))        
        self.grid = Grid2(self.canvas, 10, 10)
        
        self.canvas.create_line(0, self.height / 2, self.width, self.height / 2, fill="blue", width=1)
        self.canvas.create_line(self.width / 2, 0, self.width / 2, self.height, fill="red", width=1)

    def setup_game(self):
        #self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, "Press space to start")
        self.canvas.bind("<space>",
                         lambda _: self.start_game())

    # def add_ball(self):
    #     if self.ball is not None:
    #         self.ball.delete()
    #     paddle_coords = self.paddle.get_position()
    #     x = (paddle_coords[0] + paddle_coords[2]) / 2
    #     self.ball = Ball(self.canvas, x, 310)
    #     self.paddle.set_ball(self.ball)

    # def add_brick(self, x, y, hits):
    #     brick = Brick(self.canvas, x, y, hits)
    #     self.items[brick.item] = brick

    def draw_text(self, x, y, text, size="40"):
        font = ("Helvetica", size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        text = "Lives: %s" % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        # Unbind space so we can't start the game twice
        self.canvas.unbind("<space>")
        self.canvas.delete(self.text)
        #self.paddle.ball = None
        self.game_loop()

    def game_loop(self):
        #self.check_collisions()
        #num_bricks = len(self.canvas.find_withtag("brick"))
        # if num_bricks == 0:
        #     self.ball.speed = None
        #     self.draw_text(300, 200, "You win!")
        # If the ball has reached the bottom of the canvas
        # elif self.ball.get_position()[3] >= self.height:
        #     self.ball.speed = None
        #     self.lives -= 1
        #     if self.lives < 0:
        #         self.draw_text(300, 200, "Game over")
        #     else:
        #         # Execute self.setup_game after 1000 miliseconds
        #         self.after(1000, self.setup_game)
        # else:
        #     self.ball.update()
        
        self.grid.update()
            
        self.after(50, self.game_loop)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Hello, pong!")
    game = Game(root)

    game.mainloop()
    