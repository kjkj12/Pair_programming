import copy


class Square(object):
    orig = 0
    to = 0
    xth = 0

    def __init__(self, l):
        self.square = [l[0:3], l[3:6], l[6:9]]
        self.step = 0
        self.path = ""
        for i in range(3):
            for j in range(3):
                if self.square[i][j] == 0:
                    self.i = i
                    self.j = j

    def __eq__(self, other):  # 比较两个对象是否相等的函数
        for i in range(3):
            for j in range(3):
                if self.square[i][j] != other.square[i][j]:
                    return False
        return True

    def __hash__(self):
        t = 0
        for i in range(3):
            for j in range(3):
                t = t*10 + self.square[i][j]
        return t

    def isAns(self):
        for i in range(3):
            for j in range(3):
                if self.square[i][j] != i * 3 + j + 1 and self.square[i][j] != 0:
                    return False
        return True

    def swap(self):
        if self.step == self.xth:
            # t = self.square[int(self.orig / 3)][int(self.orig % 3)]
            # self.square[int(self.orig / 3)][int(self.orig % 3)] = self.square[int(self.to / 3)][int(self.to % 3)]
            # self.square[int(self.to / 3)][int(self.to % 3)] = t
            print("swap")

    def up_mov(self):
        if self.i != 0:
            p2 = copy.deepcopy(self)
            p2.square[p2.i][p2.j] = p2.square[p2.i - 1][p2.j]
            p2.square[p2.i - 1][p2.j] = 0
            p2.i -= 1
            p2.step += 1
            p2.path += "w"
            p2.swap()
            return p2
        else:
            return self

    def down_mov(self):
        if self.i != 2:
            p2 = copy.deepcopy(self)
            p2.square[p2.i][p2.j] = p2.square[p2.i + 1][p2.j]
            p2.square[p2.i + 1][p2.j] = 0
            p2.i += 1
            p2.step += 1
            p2.path += "s"
            p2.swap()
            return p2
        else:
            return self

    def left_mov(self):
        if self.j != 0:
            p2 = copy.deepcopy(self)
            p2.square[p2.i][p2.j] = p2.square[p2.i][p2.j - 1]
            p2.square[p2.i][p2.j - 1] = 0
            p2.j -= 1
            p2.step += 1
            p2.path += "a"
            p2.swap()
            return p2
        else:
            return self

    def right_mov(self):
        if self.j != 2:
            p2 = copy.deepcopy(self)
            p2.square[p2.i][p2.j] = p2.square[p2.i][p2.j + 1]
            p2.square[p2.i][p2.j + 1] = 0
            p2.j += 1
            p2.step += 1
            p2.path += "d"
            p2.swap()
            return p2
        else:
            return self

    def to_String(self):
        for i in range(3):
            for j in range(3):
                print(self.square[i][j], end=" ")
            print("\n", end="")
