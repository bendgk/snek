import time, os
import msvcrt as m

class Game:
    def __init__(self, size):
        self.width, self.height = size
        self.map = [[' ' for _ in range(size[0])] for _ in range(size[1])]

    def render(self):
        os.system("cls")
        print("+" * (2 + self.width))
        for i in range(self.height):
            b = "+"
            for j in range(self.width):
                b += self.map[i][j]
            print(b + "+")
        print("+" * (2 + self.width))

    def game_loop(self):
        

if __name__ == "__main__":
    game = Game((24, 8))
    game.render()
