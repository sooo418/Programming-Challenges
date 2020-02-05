dice = [[None for i in range(6)] for j in range(13)]
score = [[None for i in range(13)] for j in range(13)]
opt = [[None for i in range(15)] for j in range(8192)]
status = int()
check = [None for i in range(13)]
temp = [None for i in range(15)]

def init_input():
    global dice
    for i in range(13):
        for j in range(6):
            dice[i][j] = 0
    for i in range(13):
        input_temp = input().split()
        if not input_temp:
            return 0
        for j in range(5):
            dice[i][int(input_temp[j])-1] += 1
    return 1

def back(a):
    global status
    global opt
    global check
    global temp
    global score

    old = int()
    # 1-6번째 카테고리를 정하는 것이 아니고 이미 계산한 결과가 있으면 다시 계산하지 않는다.
    if a > 5 and opt[status][14] != -1:
        return
    
    # 12번째 카테고리를 적용할 라운드는 하나밖에 없으므로 바로 저장한다.
    if a == 12:
        for i in range(13):
            if check[i]:
                continue
            
            opt[status][a] = score[i][a]
            opt[status][14] = score[i][a]

            return
    
    # old : 현재 보고 있는 상태
    old = status
    for i in range(13):
        if check[i]:
            continue

        # status는 이미 선택된 라운드를 1로 나타낸 비트 수다.
        status += 1 << i
        check[i] = 1
        # 1-6번째 카테고리의 경우 단순 백트래킹을 하므로 백트래킹을 위해서 temp에 저장해둔다.
        temp[a] = score[i][a]
        back(a + 1)
        # 7-12번째 카테고리의 경우 메모이징을 사용한다.
        if a > 5:
            if (score[i][a] + opt[status][14]) > opt[old][14]:
                for j in range(15):
                    opt[old][j] = opt[status][j]
                opt[old][a] = score[i][a]
                opt[old][14] += score[i][a]
        # 6번째 카테고리를 결정하는 상태면 메모이징 결과와 백트래킹 결과를 병합해서 최적해와 비교한다.
        elif a == 5:
            temp[14] = 0
            for j in range(6):
                temp[14] += temp[j]
            if temp[14] >= 63:
                temp[13] = 35
            else:
                temp[13] = 0

            # 최적해는 opt[0]에 저장한다.
            if (temp[13] + temp[14] + opt[status][14]) > opt[0][14]:
                for j in range(6):
                    opt[0][j] = temp[j]
                for j in range(6, 13):
                    opt[0][j] = opt[status][j]
                opt[0][13] = temp[13]
                opt[0][14] = temp[13] + temp[14] + opt[status][14]
        check[i] = 0
        status -= 1 << i

def solve():
    global status
    global dice
    global score
    global check
    global opt

    isfullhouse = int()

    # 각 라운드의 점수를 계산한다.
    for i in range(13):
        for j in range(13):
            score[i][j] = 0
        isfullhouse = 0

        for j in range(6):
            # 1에서 6번 카테고리까지의 점수를 매긴다.
            score[i][j] = dice[i][j]*(j + 1)
            # 7번 카테고리의 점수를 구한다.
            score[i][6] += dice[i][j]*(j + 1)

            # 13번 카테고리가 가능한지를 미리 구해놓는다. 같은 수가 3개인 것 하나와 2개인 것 하나가 있어야만 만족한다.
            if dice[i][j] == 2:
                isfullhouse += 2
            if dice[i][j] == 3:
                isfullhouse += 3
        
        # 8에서 10번 카테고리의 점수를 매긴다.
        for j in range(6):
            if dice[i][j] >= 3:
                score[i][7] = score[i][6]
            
            if dice[i][j] >= 4:
                score[i][8] = score[i][6]
            
            if dice[i][j] >= 5:
                score[i][9] = 50
        
        # 11번 카테고리의 점수를 매긴다. 다음 세 가지 경우 중 하나여야만 한다.
        if (dice[i][0] and dice[i][1] and dice[i][2] and dice[i][3]) or \
            (dice[i][1] and dice[i][2] and dice[i][3] and dice[i][4]) or \
            (dice[i][2] and dice[i][3] and dice[i][4] and dice[i][5]):
            score[i][10] = 25
        
        # 12번 카테고리의 점수를 매긴다. 다음 두 가지 경우 중 하나여야만 한다.
        if (dice[i][0] and dice[i][1] and dice[i][2] and dice[i][3] and dice[i][4]) or \
            (dice[i][1] and dice[i][2] and dice[i][3] and dice[i][4] and dice[i][5]):
            score[i][11] = 35

        # 13번 카테고리의 점수를 매긴다. 앞에서 판별한 결과를 가지고 점수가 되는지를 판단한다.
        if isfullhouse == 5:
            score[i][12] = 40

    for i in range(8192):
        for j in range(15):
            opt[i][j] = 0
        opt[i][14] = -1

    for i in range(13):
        check[i] = 0
    
    status = 0
    back(0)

while init_input():
    solve()
    print('===============================================')
    for i in range(14):
        print(opt[0][i], end=' ')
    print(opt[0][14])
    print('===============================================')