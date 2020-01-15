import random

input_temp = input().split()
m = int(input_temp[0])
n = int(input_temp[1])
d = 0
while m != 0 and n != 0:
    try:
        if not(n > 0 and m <= 100):
            raise Exception("N > 0, M <= 100") # 예외발생 시 exception으로 넘어가게됨

        # 5개의 인자 중 하나를 골라 2차원 배열을 랜덤으로 생성
        mn = [[random.choice(['.','.','.','.','*']) for x in range(n)] for y in range(m)]

        # 문자열 합치기(배열이 다르면 자동으로 다음줄로 넘어간다.)
        for y in mn:
            print(''.join(y))

        # 문자열 복사
        r = mn.copy()
        
        # 지뢰의 개수 구하기
        for y, yd in enumerate(r):
            for x, xd in enumerate(yd):
                if r[y][x] == '*': continue
                count = 0
                c = [[''] if y - 1 < 0 else r[y-1][0 if x - 1 < 0 else x - 1:x+2],
                    r[y][0 if x - 1 < 0 else x - 1:x+2],
                    [''] if y + 1 >= m else r[y+1][0 if x - 1 < 0 else x - 1:x+2]]
                for z in c:
                    count+=z.count('*')
                    r[y][x] = str(count)
        d += 1
        print("Field #", end='')
        print(d, end='')
        print(':')
        for y in r:
            print(''.join(y))

        input_temp = input().split()
        m = int(input_temp[0])
        n = int(input_temp[1])
    except Exception as e:
        print('잘못 입력하셨습니다! 다시 실행해주세요...')
        print(e)