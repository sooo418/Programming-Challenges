scenario = int(input())
old_db = list()
inf_db = list()
auth_list = list()
count = 0

# ':'후에 나오는 정보를 제외시키고 새로운 리스트에 저장하기
def reduce_db():
    global old_db
    global inf_db
    for i in range(len(old_db)):
        tmp = old_db[i].split(':')
        tmp[0] += ':'
        inf_db.append(tmp[0])

# 재귀함수 호출 시 재귀함수를 호출하는 index는 제외시키기 위해 인자로 index를 갖도록 해준다.
def erdos_num(auth, index):
    global inf_db
    global count
    count += 1
    start_index = 0
    l = 0

    # 찾으려는 이름이 포함된 문장찾기
    for i in range(len(inf_db)):
        if auth in inf_db[i]:

            # 함수를 호출한 index는 넘어가도록 해준다.
            if i == index:
                continue

            # 에르되시 폴이 있을 경우 카운트 반환
            if 'Erdos, P.' in inf_db[i]:
                return count
            # 에르되시 폴이 없을 경우 존재하는 다른 이름으로 재귀함수 호출
            else:
                for j in range(len(inf_db[i])):
                    if inf_db[i][j] == ',' or inf_db[i][j] == ':':
                        l += 1
                        if l == 2:
                            other = inf_db[i][start_index:j]
                            start_index = j + 2
                            l = 0

                            # 인자로 들어온 저자의 이름은 넘어가도록 해준다.
                            if other == auth:
                                continue
                            result = erdos_num(other, i)
                            if result:
                                return result

    return 0



for t in range(scenario):
    # 시나리오, p n 입력
    tmp = input().split()
    p = int(tmp[0])
    n = int(tmp[1])

    # 논문 정보 입력
    for i in range(p):
        inf = str(input())
        old_db.append(inf)

    reduce_db()

    # 에르되시 수를 알고싶은 저자의 이름을 입력
    for i in range(n):
        auth = str(input())
        auth_list.append(auth)
    print('')
    print("Scenario", end=' ')
    print(t + 1)
        
    for i in range(n):
        value = erdos_num(auth_list[i], None)
        count = 0
        if value:
            print(auth_list[i], end=' ')
            print(value)
        else:
            print(auth_list[i], end=' ')
            print('infinity')
