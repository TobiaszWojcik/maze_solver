from PIL import Image
from os.path import exists


class Maze:
    def __init__(self, filename):
        self.h = 0
        self.w = 0
        self.filename = filename
        self.image_data = None
        self.maze = []

    def load_image(self):
        if exists(self.filename):
            try:
                file = Image.open(self.filename)
                self.image_data = list(file.getdata())
                self.w = file.width
                self.h = file.height
                print(f'Loaded image {self.w} x {self.h} px')

            except IOError:
                print("Error with reading image file")
                return False
        else:
            print(f'Image file "{self.filename}" not found')
            return False
        return True

    def make_maze(self):
        if self.image_data:
            temp_data = []
            for i, field in enumerate(self.image_data):
                value = 0
                if field == (255, 255, 255):
                    value = 6
                elif field == (0, 0, 0):
                    value = 8
                elif field == (255, 0, 0):
                    value = 10
                elif field == (0, 255, 0):
                    value = 11
                else:
                    value = 6
                self.maze.append([value, [0, 0]])
            self.maze = [self.maze[i:i + self.w] for i in range(0, len(self.maze), self.w)]
            print('Maze was made')
            return True

        else:
            print('Image not loaded, use ".load_image()" method')
            return False

