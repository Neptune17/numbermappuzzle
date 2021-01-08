from painter import *
import time

def DFS(Map, YStack, YStack_bound, x, y, layer):
    if layer == len(x):
        return True

    global_check = True
    for i in range(len(y)):
        if YStack[i] != len(y[i]) and YStack_bound[i][YStack[i]] < layer:
            global_check = False
            break

    if not global_check:
        return False

    # print("layer: " + str(layer), x[layer])

    state = [0 for i in range(len(x[layer]))]
    end_state = [0 for i in range(len(x[layer]))]
    pre_end = 0
    pre_start = len(x) - x[layer][-1]
    for i in range(len(x[layer])):
        state[i] = pre_end
        pre_end += x[layer][i] + 1
    for i in range(len(x[layer]) - 1, -1, -1):
        end_state[i] = pre_start
        if i - 1 >= 0:
            pre_start -= x[layer][i - 1] + 1
    
    # print(state)
    # print(end_state)

    while(True):
        # convert current state
        templayer = [0 for i in range(len(x))]
        
        for i in range(len(state)):
            for j in range(state[i], state[i] + x[layer][i]):
                templayer[j] = 1
        
        # print(templayer)

        # check current state
        local_check = True
        for i in range(len(x)):
            if templayer[i] == 0 and Map[layer][i] == -1:
                local_check = False
                break
            if templayer[i] == 1 and Map[layer][i] == 0:
                if YStack[i] == len(y[i]):
                    local_check = False
                    break
                if layer > 0 and Map[layer - 1][i] == 1:
                    local_check = False
                    break

        # if check ok, move to next layer
        if local_check:
            save_layer = [Map[layer][i] for i in range(len(x))]
            for i in range(len(x)):
                if templayer[i] == 1 and save_layer[i] == 0:
                    ysize = y[i][YStack[i]]
                    YStack[i] += 1
                    for j in range(layer, layer + ysize):
                        Map[j][i] = -1
                Map[layer][i] = templayer[i]
            ret = DFS(Map, YStack, YStack_bound, x, y, layer + 1)
            if ret:
                return True
            for i in range(len(x)):
                if templayer[i] == 1 and save_layer[i] == 0:
                    YStack[i] -= 1
                    ysize = y[i][YStack[i]]
                    for j in range(layer, layer + ysize):
                        Map[j][i] = 0
                Map[layer][i] = save_layer[i]

        # final state, return to pre layer
        if state == end_state:
            break
            
        # move to next state
        for i in range(len(state) - 1, -1, -1):
            if state[i] != end_state[i]:
                state[i] = state[i] + 1
                for j in range(i + 1 , len(state)):
                    state[j] = state[j - 1] + x[layer][j - 1] + 1
                break

    return False

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
    # row = [
    #     [4],
    #     [6,4],
    #     [12,1],
    #     [2,1,6],
    #     [2,5,1],
    #     [3,1,6],
    #     [3,7],
    #     [3,6],
    #     [3,1,5,1],
    #     [2,6],
    #     [12,1],
    #     [6,4],
    #     [4],
    #     [3],
    #     [5]
    # ]

    # col = [
    #     [7],
    #     [9],
    #     [2,4,2],
    #     [2,2],
    #     [2,1,1,2],
    #     [3,2],
    #     [2,2],
    #     [3,3,1],
    #     [9,1],
    #     [9,1],
    #     [11,2],
    #     [15],
    #     [14],
    #     [2,3,2],
    #     [1,1,1,1,1,1,1]
    # ]

    # row = [
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

    # col = [
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

    row = [
        [1,1,1],
        [2,1,2,2],
        [1,1,5,1],
        [1,3,1],
        [1,1,3,3,1],
        [3,1],
        [5,1],
        [2,1,2,1],
        [1,1,1],
        [5,1,2],
        [2,4,1,2],
        [1,2,2,2],
        [1,2,1,2,3],
        [1,6,1],
        [13,1]
    ]
    
    col = [
        [1,1,1,3,1],
        [1,2,1],
        [1,1,1,1,4],
        [1,2,1],
        [2,1],
        [1,1,1,2,1,1],
        [2,1,2,2,1],
        [5,6],
        [4,4,3],
        [5,1,2],
        [2,1,2,2],
        [1,1,1,3],
        [5],
        [4,4],
        [2,5,2]
    ]

    rowlabel, collabel = generate_label(row, col)
    AnsMap = np.zeros((len(row),len(col)))
    ColStack = [0 for i in range(len(col))]
    ColStack_bound = []
    for i in range(len(col)):
        ColStack_bound.append([0 for i in range(len(col[i]))])
        pre_start = len(row) - col[i][-1]
        for j in range(len(col[i]) - 1, -1, -1):
            ColStack_bound[i][j] = pre_start
            if j - 1 >= 0:
                pre_start -= col[i][j - 1] + 1

    begin = time.time()
    ret = DFS(AnsMap, ColStack, ColStack_bound, row, col, 0)
    end = time.time()
    
    print("time:", end - begin, ret)
    paint_map(AnsMap.T, rowlabel, collabel, "result.jpg")