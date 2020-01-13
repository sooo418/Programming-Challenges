max_s = 10
max_digits = 8
hor_bar = []
ver_bar = [" ", "|"]

# 숫자의 디스플레이값
hor = [[1,0,1], [0,0,0], [1,1,1], [1,1,1], [0,1,0], [1,1,1], [1,1,1], [1,0,0], [1,1,1], [1,1,1]]
ver = [[1,1,1,1], [0,1,0,1], [0,1,1,0], [0,1,0,1], [1,1,0,1], [1,0,0,1], [1,0,1,1], [0,1,0,1], [1,1,1,1], [1,1,0,1]]

s = int(input('크기를 입력해주세요 : '))
while s != 0:
    result = [[],[],[],[],[]]
    r = []
    tmp1 = ''
    tmp2 = ''
    for i in range(s):
        tmp1 += ' '
        tmp2 += '-'
    hor_bar.append(tmp1)
    hor_bar.append(tmp2)
    number = str(input('출력할 숫자를 입력해주세요 : '))
    num_digits = len(number)
    for i in range(num_digits):
        digit = int(number[i])
        if i > 0:
            for j in range(5):
                result.append(" ")
        
        # 0번 - 맨 윗줄 가로 bar
        result[0].append(' ')
        result[0].append(hor_bar[hor[digit][0]])
        result[0].append(' ')
        # 1번 - 위쪽 세로 bar들
        result[1].append(ver_bar[ver[digit][0]])
        result[1].append(hor_bar[0])
        result[1].append(ver_bar[ver[digit][1]])
        # 2번 - 맨 윗줄 가로 bar
        result[2].append(' ')
        result[2].append(hor_bar[hor[digit][1]])
        result[2].append(' ')
        # 3번 - 위쪽 세로 bar들
        result[3].append(ver_bar[ver[digit][2]])
        result[3].append(hor_bar[0])
        result[3].append(ver_bar[ver[digit][3]])
        # 4번 - 맨 윗줄 가로 bar
        result[4].append(' ')
        result[4].append(hor_bar[hor[digit][2]])
        result[4].append(' ')

    r.append(result[0])
    for i in range(s):
        r.append(result[1])
    r.append(result[2])
    for i in range(s):
        r.append(result[3])
    r.append(result[4])
    
    for y in r:
        print(''.join(y))
    
    hor_bar = []
    s = int(input('크기를 입력해주세요 : '))