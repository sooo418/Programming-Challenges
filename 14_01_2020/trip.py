while(1):
    # input
    n = int(input('사람수를 입력하세요 : '))
    if n == 0: break
    cost = []
    for i in range(n):
        tmp1 = float(input('각자의 비용을 입력하세요 : '))
        cost.append(tmp1)

    # 비용의 평균 구하기
    cost_avg = sum(cost) // n

    # 비용의 평균보다 비용을 덜 낸 사람들의 비용을 평균에서 빼고 총합 구하기
    difference = []
    for i in cost:
        if cost_avg > i:
            tmp2 = cost_avg - i
            difference.append(tmp2)
    result = sum(difference)
    print(result)