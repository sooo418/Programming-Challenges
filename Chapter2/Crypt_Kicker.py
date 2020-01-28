dic = list()
line = str()
n = int()

# 암호문 line의 k번째 위치 이후에 처음 나타나는 단어를 사전의 단어와 일치시켜 보고, map/inv와 일관되는 mapping인지 검사하면서 계속 탐색한다.
def search(k, map1, inv1):
    global line
    global n
    global dic
    word = list()
    map2 = dict()
    inv2 = dict()
    b = bool()
    t = 0

    while k < 42 and line[k] == ' ':
        k += 1

    if k >= len(line):  # 문장 끝까지 도달했음
        # 평문을 출력하고 돌아간다.
        for i in range(len(line)):
            print(' ' if line[i] == ' ' else map1[line[i]], end='')
        print('')
        return 1

    # k번째 위치 이후의 첫번째 단어를 얻어낸다.
    while k + t < 42  and line[k + t] >= 'a' and line[k + t] <= 'z':
        word.append(line[k + t])
        t += 1
    
    for i in dic:
        b = True
        # 사전에서 길이가 같은 단어를 검색
        if len(i) == len(word):
            map2 = map1
            inv2 = inv1
            # word를 dic[i]에 일치시키면서, mapping의 일관성이 유지되는지 검사한다.
            for j in range(len(word)):
                # 일관성을 깨뜨리는 두 가지 조건 검사
                if map2[word[j]] and map2[word[j]] != i[j] or \
                    inv2[i[j]] and inv2[i[j]] != word[j]:
                    b = False
                    break
                else:
                    # mapping을 업데이트한다.
                    map2[word[j]] = i[j]
                    inv2[i[j]] = word[j]
            # word를 dic[i]에 일치시킬 수 있는 경우 다음 단어를 찾기 위해 탐색을 계속한다.
            if b and search(k + t, map2, inv2):
                return 1
            
    return 0

n = int(input())
map1 = dict()
inv1 = dict()
for i in range(n):
    if n > 1000:
        print('1000개를 넘길 수 없습니다')
        break
    tmp = str(input())
    if len(tmp) <= 16:
        dic.append(tmp.lower())
line = str(input())
while line != '':
    if len(line) <= 80:
        line = line.lower()
        for i in range(ord('a'), ord('z')+1):
            map1[chr(i)] = None
            inv1[chr(i)] = None
        if not search(0, map1, inv1):
            for i in range(len(line)):
                print(' ' if line[i] == ' ' else '*', end='')
            print('')
        line = str(input())