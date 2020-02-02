seq = list()
jolly_seq = list()
dif_list = list()
input_temp = input().split()
n = int(input_temp[0])
if n <= 3000:
    # 유쾌한 점퍼 수열
    for i in range(1,n):
        jolly_seq.append(i)

    # 유쾌한 점퍼인지 비교할 수열생성
    for i in range(1, n):
        dif = abs(int(input_temp[i]) - int(input_temp[i+1]))
        dif_list.append(dif)
dif_list.sort()

if jolly_seq == dif_list:
    print('Jolly')
else:
    print('Not jolly')