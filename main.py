
from random import randint
from time import sleep
import os
from img_to_maze import Maze


print("""This is my maze solver program:)\n
    Prepare your maze according to the instructions below\n
    To see the whole maze, adjust the image resolution to your monitor.\n
    With a full HD monitor, the largest size is 200 x 50 pixels.\n
    In the image in the RGB palette, select:\n
    Black pixels as walls - RGB (0,0,0) #000000\n
    Green pixels as meta - RGB(0,255,0) #00FF00\n
    Red pixels as start - RGB(255,0,0) # FF0000\n
    The other colors are empty spots.\n
    Place the graphic file with the maze in the folder with the program.\n\n""")


def print_map(step=0, back=False):
    print(f'This is step:{step}')
    print("-" * (map_row+2))
    for x in map:
        print("|", end="")
        for y in x:
            if y[0] == 11:
                print("O", end="")
            elif y[0] == 12:
                print("*", end="")
            elif y[0] == 10:
                print("X", end="")
            elif y[0] == 9:
                if back:
                    print(" ",end="")
                else:
                    print("+", end="")
            elif y[0] < 7:
                print(" ",end="")
            else:
                print("█",end="")
        print("|")
    print("-" * (map_row+2))


def do_step_back(end):
    print(end)
    if not map[end[0]][end[1]][0] == 10:
        map[end[0]][end[1]][0] = 12
    end = map[end[0]][end[1]][1]
    return end


def do_step():
    change_list = []
    for x in range(0, map_col):
        for y in range(0, map_row):
            if map[x][y][0] == 11 or map[x][y][0] == 9:
                if y > 0:
                    if map[x][y-1][0] < 7 or map[x][y-1][0] == 10:
                        map[x][y - 1][1][0] = x
                        map[x][y - 1][1][1] = y
                        change_list.append([x, y - 1])
                if y < map_row-1:
                    if map[x][y + 1][0] < 7 or map[x][y+1][0] == 10:
                        map[x][y + 1][1][0] = x
                        map[x][y + 1][1][1] = y
                        change_list.append([x, y + 1])
                if x > 0:
                    if map[x - 1][y][0] < 7 or map[x - 1][y][0] == 10:
                        map[x - 1][y][1][0] = x
                        map[x - 1][y][1][1] = y
                        change_list.append([x - 1, y])
                if x < map_col - 1:
                    if map[x + 1][y][0] < 7 or map[x + 1][y][0] == 10:
                        map[x + 1][y][1][0] = x
                        map[x + 1][y][1][1] = y
                        change_list.append([x + 1, y])
    for field in change_list:

        if map[field[0]][field[1]][0] == 10:
            return [2, [field[0], field[1]]]
        # if map[field[0]][field[1]] < 7:
        map[field[0]][field[1]][0] = 9

    print(f'Zajęte pola {len(change_list)}')
    if len(change_list) == 0:
        return [1]
    return [0]


maze = Maze(input("Enter here the file name with extension format and press <Enter>"))

map = None

if maze.load_image():
    if maze.make_maze():
        map_row = maze.w
        map_col = maze.h
        map = maze.maze
        start = [30, 150]
        end = [22, 13]
        sleep(3)
    #Map generator
    # for x in range(0, map_col):
    #     rowfields=[]
    #     for y in range(0, map_row):
    #         fieldtype = randint(3,8)
    #         rowfields.append([fieldtype,[0,0]])
    #     map.append(rowfields)
    #
    # map[start[0]][start[1]][0] = 11
    # map[end[0]][end[1]][0] = 10


        i = 0

        while True:
            i += 1

            os.system("clear")
            finish = do_step()

            print_map(i)
            if finish[0]:
                if finish[0] == 1:
                    print("Brak dalszego ruchu - koniec poszukiwań")
                else:
                    end = finish[1]
                    print(f'Wytropiony w {i} krokach. Teraz powrót')
                    sleep(1)
                    while True:
                        os.system("clear")
                        end = do_step_back(end)
                        if map[end[0]][end[1]][0] == 11:
                            print_map(i, True)
                            print("Koniec!")
                            break
                        print_map(i, True)
                        sleep(0.02)

                break
            sleep(0.05)
input("Press <Enter> to exit")

