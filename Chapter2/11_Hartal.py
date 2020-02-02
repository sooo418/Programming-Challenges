num_case = int(input())
hartal_day = list()
result = list()
while num_case > 0:
    day = int(input())
    if day < 7 or day > 3650:
        print('정해진 일 수를 초과하였습니다.')
        break
    num_hartal = int(input())
    for i in range(num_hartal):
        tmp = int(input())
        hartal_day.append(tmp)
    for i in range(num_hartal):
        for j in range(hartal_day[i],day+1,hartal_day[i]):
            if j % 7 == 6 or j % 7 == 0:
                print(j)
                continue
            if len(result) != 0:
                if j in result:
                    pass
                else:
                    result.append(j)
            else:
                result.append(j)
    print('손실된 근무 일수: ', end='')
    print(len(result))
    hartal_day.clear()
    result.clear()
    num_case -= 1