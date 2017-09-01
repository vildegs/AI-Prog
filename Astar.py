


def heuristic():
    h = 0
    h+=4-positions1[0]
    for i in range(positions1[0]+carSize1-1):
        if board1[fixedPos1[0]][positions1[0]+carSize1+i] != '.':
            h +=1
    return h

board1 = [['.' for i in range(6)] for j in range (6)]

fixedPos1 = [2, 2]
positions1= [0, 2]
carSize1 = 2
board1[2][0], board1[2][1] = 0, 0
board1[2][2], board1[3][2] = 1, 1


def main():
    print(heuristic())


main()
