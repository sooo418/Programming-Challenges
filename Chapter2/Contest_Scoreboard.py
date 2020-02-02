score_board = [[0 for i in range(10)]for j in range(101)]
sum_score = 0
penalty = 0
count = 0

num_case = int(input())
print('')
while num_case > 0:
    line = input().split()
    while line:
        team_num = int(line[0])
        exam_num = int(line[1])
        time = int(line[2])
        l = line[3]
        if l == 'C':
            score_board[team_num][exam_num] = time
        elif l == 'I':
            score_board[team_num][0] += 20
        elif l == 'R' or l == 'U' or l == 'E':
            score_board[team_num][exam_num] = 0
        print('')
        line = input().split()

    for i in range(1, 101):
        for j in range(10):
            if j == 0:
                penalty = score_board[i][j]
            elif j > 0 and score_board[i][j] != 0:
                count += 1
                sum_score += score_board[i][j]
        if sum_score != 0:
            print(i, end=' ')
            print(count, end=' ')
            print(sum_score + penalty)
            print('')
        sum_score = 0
        count = 0
        penalty = 0
    num_case -= 1