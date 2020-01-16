matrix = list()
# F 명령어의 R영역을 채워주는 기능을 하는 함수
def fill(col, row, org_color, color):
    global matrix
    matrix[col-1][row-1] = color
    m = len(matrix)
    n = len(matrix[0])

    if col > 1 and matrix[col-2][row-1] == org_color:
        fill(col-1, row, org_color, color)
    if col < m and matrix[col][row-1] == org_color:
        fill(col+1, row, org_color, color)
    if row > 1 and matrix[col-1][row-2] == org_color:
        fill(col, row-1, org_color, color)
    if row < n and matrix[col-1][row] == org_color:
        fill(col, row+1, org_color, color)

command = ''
while command != 'X':
    instruction = input()
    instruction_list = instruction.split()
    command = instruction_list[0]

    # 하나의 픽셀그래픽을 생성해주는 명령어 I
    if command == 'I':
        m = int(instruction_list[1])
        n = int(instruction_list[2])
        matrix = [['O' for col in range(m)] for row in range(n)]

    # 픽셀그래픽의 모든 픽셀을 'O'로 바꿔주는 명령어 C
    elif command == 'C':
        for i in range(n):
            for j in range(m):
                matrix[i][j] = 'O'

    # 선택된 픽셀의 색깔을 바꿔주는 명령어 L
    elif command == 'L':
        x = int(instruction_list[1])
        y = int(instruction_list[2])
        c = instruction_list[3]
        matrix[y-1][x-1] = c

    # X열의 Y1부터 Y2까지 색깔을 바꿔주는 명령어 V
    elif command == 'V':
        x = int(instruction_list[1])
        y1 = int(instruction_list[2])
        y2 = int(instruction_list[3])
        c = instruction_list[4]
        for i in range(y1, y2+1):
            matrix[i-1][x-1] = c

    # Y행의 X1부터 X2까지 색깔을 바꿔주는 명령어 H
    elif command == 'H':
        x1 = int(instruction_list[1])
        x2 = int(instruction_list[2])
        y = int(instruction_list[3])
        c = instruction_list[4]
        for i in range(x1, x2+1):
            matrix[y-1][i-1] = c

    # 주어진 색으로 직사각형을 그려주는 명령어 K
    elif command == 'K':
        x1 = int(instruction_list[1])
        y1 = int(instruction_list[2])
        x2 = int(instruction_list[3])
        y2 = int(instruction_list[4])
        c = instruction_list[5]
        for col in range(y1, y2+1):
            for row in range(x1, x2+1):
                matrix[col-1][row-1] = c

    # R영역을 주어진 색으로 채우는데 선택된 픽셀의 맞닿은 픽셀들의 색깔이 선택된 픽셀의 색깔이 같으면 주어진 색으로 바꿔주는 명령어 F
    elif command == 'F':
        x = int(instruction_list[1])
        y = int(instruction_list[2])
        c = instruction_list[3]
        fill(y, x, matrix[y-1][x-1], c)

    # 입력한 파일명을 출력하고 현재 이미지의 내용을 출력해주는 명령어 S
    elif command == 'S':
        file_name = instruction_list[1]
        print(file_name)
        for i in matrix:
            print(''.join(i))