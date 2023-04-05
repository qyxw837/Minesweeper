import minemap
import numpy as np

map1 = minemap.Minemap(9, 9, 10)
map_click = np.zeros((map1.width, map1.height), dtype=int)

def map_play():
    game_over_flag = 0
    x, y = map(int, input("请输入坐标: ").split())
    for i in range(map1.height):
        for j in range(map1.width):
            if map_click[j][i] == 0:
                print("?", end=" ")
            elif map_click[j][i] == 1:
                print(map1.mine_map[j][i], end=" ")
        print()
        map_click[x][y] = 1

    if map1.mine_map[x][y] == -1:
        game_over_flag = 1
        return game_over_flag
    elif map1.mine_map[x][y] == 0: 
        click_zero(x, y)
    if np.sum(map_click == 1) == map1.width * map1.height - map1.mine_num:
        game_over_flag = 2
        return game_over_flag

def click_zero(x, y): # 点击到空白区域, 使用宽度优先算法递归周围8个格子
    que = []
    que.append([x, y])
    while que:
        x, y = que.pop(0)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i < 0 or x + i >= map1.width or y + j < 0 or y + j >= map1.height:
                    continue
                if map_click[x + i][y + j] == 0:
                    map_click[x + i][y + j] = 1
                    if map1.mine_map[x + i][y + j] == 0:
                        que.append([x + i, y + j])

while 1:
    flag = map_play()
    if flag == 1:
        map1.map_print()
        print()
        print("Game Over!")
        break
    elif flag == 2:
        map1.map_print()
        print("You Win!")
        break