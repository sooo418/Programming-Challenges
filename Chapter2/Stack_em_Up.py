shuffle = list()
old_deck = list()
temp_deck = list()

num_case = int(input())
print('')

while num_case > 0:
    num_shuffle = int(input())
    # 섞는 방법들을 입력
    if num_shuffle > 100:
        print('100개를 넘길 수 없습니다!!')
        break
    for i in range(num_shuffle):
        tmp = input().split()
        for j in range(len(tmp)):
            temp_deck.append(int(tmp[j]))
        shuffle.append(temp_deck.copy())
        temp_deck.clear()
    # 새로운 패
    deck = [i for i in range(1,53)]

    # 카드를 섞는다
    shuffle_exe = input()
    while shuffle_exe != '':
        shuffle_exe = int(shuffle_exe)
        old_deck = deck.copy()
        for i in range(len(deck)):
            deck[i] = old_deck[shuffle[shuffle_exe-1][i]-1]
    
        shuffle_exe = input()

    num_case -= 1
    if num_case > 0:
        print('')
    
    for i in range(len(deck)):
        value = (deck[i] - 1) % 13
        suit = (deck[i] - 1) // 13
        if value == 9:
            print('Jack', end=' ')
        elif value == 10:
            print('Queen', end=' ')
        elif value == 11:
            print('King', end=' ')
        elif value == 12:
            print('Ace', end=' ')
        else:
            print(value + 2, end=' ')
        print('of', end=' ')
        if suit == 0:
            print('Clubs')
        elif suit == 1:
            print('Diamonds')
        elif suit == 2:
            print('Hearts')
        elif suit == 3:
            print('Spaces')