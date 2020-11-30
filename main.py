from painter import *
import time

def check(x, cnt):
    temp = cnt
    index = -1
    for i in x:
        if temp == 0:
            return 1
        if temp < 0:
            return 2
        temp -= i
    if temp < 0:
        return 2
    if temp == 0:
        return 3

def DFS1(mat, x, y, line, loc, available, mark):
    if len(y[line]) == loc:
        return DFS(mat, x, y, line + 1, mark)
    for i in range(available, len(x)):
        flag = True
        for j in range(i, i + y[line][loc]):
            if j >= len(x):
                flag = False
                continue
            if check(x[j], mark[j]) == 1 and (line > 0 and mat[j,line - 1] == 1):
                flag = False
            if check(x[j], mark[j]) == 2 and (line == 0 or mat[j,line - 1] == 0):
                flag = False
            if check(x[j], mark[j]) == 3:
                flag = False
            mat[j, line] = 1
            mark[j] += 1
        if flag:
            ret = DFS1(mat, x, y, line, loc + 1, i + y[line][loc] + 1, mark)
            if ret:
                return ret
        for j in range(i, i + y[line][loc]):
            if j >= len(x):
                continue
            mat[j, line] = 0
            mark[j] -= 1
    return False

def DFS(mat, x, y, line, mark):
    if line == len(y):
        return True
    return DFS1(mat, x, y, line, 0, 0, mark)

def generate_label(x, y):
    xlabel = []
    for i in range(len(x)):
        line = ""
        for j in range(len(x[i]) - 1):
            line += str(x[i][j])
            line += " "
        line += str(x[i][len(x[i]) - 1])
        xlabel.append(line)
    ylabel = []
    for i in range(len(y)):
        line = ""
        for j in range(len(y[i]) - 1):
            line += str(y[i][j])
            line += " "
        line += str(y[i][len(y[i]) - 1])
        ylabel.append(line)
    return xlabel, ylabel

if __name__ == '__main__':
    x = [
        [4],
        [6,4],
        [12,1],
        [2,1,6],
        [2,5,1],
        [3,1,6],
        [3,7],
        [3,6],
        [3,1,5,1],
        [2,6],
        [12,1],
        [6,4],
        [4],
        [3],
        [5]
    ]

    y = [
        [7],
        [9],
        [2,4,2],
        [2,2],
        [2,1,1,2],
        [3,2],
        [2,2],
        [3,3,1],
        [9,1],
        [9,1],
        [11,2],
        [15],
        [14],
        [2,3,2],
        [1,1,1,1,1,1,1]
    ]

    # x = [
    #     [2],
    #     [4,2],
    #     [1,2,1],
    #     [1,1,1,3],
    #     [3,5],
    #     [2,2,1],
    #     [2,1,1,2],
    #     [6],
    #     [2,1],
    #     [2]
    # ]

    # y = [
    #     [2,3],
    #     [1,5],
    #     [1,2,2],
    #     [1,1,2],
    #     [2,1],
    #     [6],
    #     [2],
    #     [1,2],
    #     [2,2,1,1],
    #     [6,2]
    # ]
    
    xlabel, ylabel = generate_label(x, y)
    mat=np.zeros((len(x),len(y)))
    begin = time.time()
    print(DFS(mat, x, y, 0, [0 for i in range(len(x))]))
    end = time.time()
    print("time:", end - begin)
    paint_map(mat.T, xlabel, ylabel, "result.jpg")