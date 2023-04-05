import random
import numpy as np

class Minemap:
    def __init__(self, width, height, mine_num):
        self.width = width
        self.height = height
        self.mine_num = mine_num
        self.mine_map = np.zeros((width, height), dtype=int)

        mine_list = random.sample(range(0, self.height * self.width), mine_num)
        for i in mine_list:
            self.mine_map[i // self.width][i % self.height] = -1 # 随机生成雷, 以-1表示

        for i in range(self.height):
            for j in range(self.width):
                if self.mine_map[j][i] == -1:
                    continue
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if j + k < 0 or j + k >= self.width or i + l < 0 or i + l >= self.height: # 越界判断
                            continue
                        if self.mine_map[j + k][i + l] == -1: # 计算周围8个格子几个是雷
                            self.mine_map[j][i] += 1

    def map_print(self): # 打印地图, 用于测试
        for i in range(self.height):
            for j in range(self.width):
                if self.mine_map[j][i] == -1:
                    print("X", end=" ") # 雷用X表示
                else:
                    print(self.mine_map[j][i], end=" ")
            print()

def main():
    example = Minemap(9, 9, 10)
    example.map_print()

if __name__ == "__main__":
    main()