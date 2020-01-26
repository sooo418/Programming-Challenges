max_votes = 1000
max_candidate = 20
max_name_length = 80
who_got_max = 0
cand_list = list()
vote_list = list()
index_of_1st_alive = list()
num_case = int(input())
print('')
while num_case > 0:
    num_cand = int(input())
    if num_cand > 20:
        print('후보자는 20명을 넘길 수 없습니다!!')
        break
    popularity = [0 for i in range(num_cand)]
    for i in range(num_cand):
        cand_name = str(input())
        if len(cand_name) > 80:
            print('후보자의 이름을 80자 이내로 입력해주세요!!')
            break
        cand_list.append(cand_name)
    
    # 투표시작
    vote = input().split()
    num_vote = 0
    while vote and num_vote <= 1000:
        num_vote += 1
        if len(vote) != num_cand:
            print('후보자 모두에게 순위를 매겨주세요!!')
            break

        # 투표 리스트에 투표추가하기
        line = []
        for i in range(len(vote)):
            line.append(vote[i])
        vote_list.append(line)
        
        # 1순위로 뽑힌 후보자의 득표 수 증가
        popularity[int(vote[0])-1] += 1

        index_of_1st_alive.append(0)
        
        vote = input().split()
    
    # 당선자 구하기
    max_pop = -1
    min_pop = max_votes + 1
    # all_tied ==> 동률일 경우
    all_tied = 1
    while True:
        for i in range(num_cand):
            if popularity[i] > 0:
                # 아직 탈락되지 않은 후보자들만
                
                # 최다득표자인지 검사
                if popularity[i] > max_pop:     # 동률 제거
                    if max_pop >= 0:
                        all_tied = 0
                    max_pop = popularity[i]

                    # 최다투표자 기록
                    who_got_max = i
                
                # 최소득표자인지 검사
                if popularity[i] < min_pop:     # 동률 제거
                    if min_pop <= max_votes:
                        all_tied = 0
                    min_pop = popularity[i]

        # 과반득표자 또는 동률이거나 만장일치일 경우
        if max_pop * 2 > num_vote or all_tied:
            break

        # 최소득표자를 제거하기 위한 처리 각 투표용지를 하나씩 점검하면서, 현재 최소득표자에게 돌아가 있는 표는 걸러내어
        # 이 투표용지에서 그 다음으로 선호도가 높은 후보에게 넘겨준다.
        for i in range(num_vote):
            # 현재 이 투표용지를 받은 후보자가 최소득표자인지 검사
            if popularity[int(vote_list[i][index_of_1st_alive[i]])-1] == min_pop:
                # 그 다음으로 선호하는 후보자를 찾는다.
                index_of_1st_alive[i] += 1
                while True:
                    if popularity[int(vote_list[i][index_of_1st_alive[i]])-1] >= min_pop:
                        break
                    index_of_1st_alive[i] += 1
                # 이 후보에게 투표용지를 하나 추가
                popularity[int(vote_list[i][index_of_1st_alive[i]])-1] += 1
            
        # 최소득표자의 득표를 0으로 리셋한다.
        for i in range(num_cand):
            if popularity[i] == min_pop:
                popularity[i] = 0

    if max_pop * 2 > num_vote:
        # 과반득표자가 있는 경우
        print(cand_list[who_got_max])
    else:
        # 그렇지 않으면 현재 '살아남은' 모든 후보자들을 출력
        for i in range(num_cand):
            if popularity[i] > 0:
                print(cand_list[i])
    
    num_case -= 1
    if num_case > 0:
        print('')