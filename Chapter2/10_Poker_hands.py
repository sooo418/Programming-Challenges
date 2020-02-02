def get_value(x):
    return x // 10
def get_suit(x):
    return x % 10
black_hands_score = list()  # black카드의 족보와 비교할 카드의 값을 저장할 리스트
white_hands_score = list()  # white카드의 족보와 비교할 카드의 값을 저장할 리스트
black_value = list()        # black카드의 값들을 저장하는 리스트
white_value = list()        # white카드의 값들을 저장하는 리스트
hands = input().split()

# 문자열 형태의 카드 값을 숫자 표현으로 변환
def encode_card(card):
    result = 0
    if card[0] == 'T':
        result = 100
    elif card[0] == 'J':
        result = 110
    elif card[0] == 'Q':
        result = 120
    elif card[0] == 'K':
        result = 130
    elif card[0] == 'A':
        result = 140
    else:
        result = int(card[0]) * 10
    
    if card[1] == 'H':
        result += 1
    elif card[1] == 'D':
        result += 2
    elif card[1] == 'S':
        result += 3
    elif card[1] == 'C':
        result += 4
    return result
        
def get_hands_score(hands):
    value = list()
    suit = list()
    result = list()
    for i in range(5):
        value.append(get_value(hands[i]))
        suit.append(get_suit(hands[i]))
    # 스트레이트 플러시
    if value[1] + 1 == value[0] and suit[1] == suit[0] and \
        value[2] + 2 == value[0] and suit[2] == suit[0] and \
        value[3] + 3 == value[0] and suit[3] == suit[3] and \
        value[4] + 4 == value[0] and suit[4] == suit[4]:
        
        result.append(9)
        result.append(value[0])

    # 포카드 - 정렬된 상태이므로 카드를 일일히 세지 않고도 1,4번째 카드가 같거나 또는 2,5번째 카드가 같은지만 검사하면 된다.
    elif value[0] == value[3] or value[1] == value[4]:
        
        result.append(8)
        result.append(value[0])

    # 풀하우스 - 2장+3장 또는 3장+2장 형태이므로 다음과 같이 아주 간단하게 검사할 수 있다.
    elif value[0] == value[2] and value[3] == value[4]:
        
        result.append(7)
        result.append(value[0])

    elif value[0] == value[1] and value[2] == value[4]:
        
        result.append(7)
        result.append(value[2])

    # 플러시
    elif suit[1] == suit[0] and suit[2] == suit[0] and \
        suit[3] == suit[0] and suit[4] == suit[0]:

        result.append(6)
        for i in range(5):
            result.append(value[i])

    # 스트레이트
    elif value[1] + 1 == value[0] and value[2] + 2 == value[0] and \
        value[3] + 3 == value[0] and value[4] + 4 == value[0]:
        
        result.append(5)
        result.append(value[0])

    # 쓰리카드
    elif value[0] == value[2] or \
        value[1] == value[3] or \
        value[2] == value[4]:

        result.append(4)
        result.append(value[2])

    # 투페어 - 다음과 같이 세가지 가능성만 존재한다.
    elif value[0] == value[1] and value[2] == value[3]:

        result.append(3)
        result.append(value[0])
        result.append(value[2])
        result.append(value[4])

    elif value[0] == value[1] and value[3] == value[4]:

        result.append(3)
        result.append(value[0])
        result.append(value[3])
        result.append(value[2])

    elif value[1] == value[2] and value[3] == value[4]:

        result.append(3)
        result.append(value[1])
        result.append(value[3])
        result.append(value[0])

    # 원페어
    elif value[0] == value[1]:

        result.append(2)
        result.append(value[0])
        result.append(value[2])
        result.append(value[3])
        result.append(value[4])

    elif value[1] == value[2]:

        result.append(2)
        result.append(value[1])
        result.append(value[0])
        result.append(value[3])
        result.append(value[4])

    elif value[2] == value[3]:

        result.append(2)
        result.append(value[2])
        result.append(value[0])
        result.append(value[1])
        result.append(value[4])

    elif value[3] == value[4]:

        result.append(2)
        result.append(value[3])
        result.append(value[0])
        result.append(value[1])
        result.append(value[2])

    # 하이카드
    else:
        result.append(1)
        for i in range(5):
            result.append(value[i])
    
    return result

def hands_compare(black, white):
    if black[0] > white[0]:
        print('Black wins.')
    
    elif black[0] < white[0]:
        print('White wins.')
    
    else:
        length = len(black)
        for i in range(1, length):
            if black[i] > white[i]:
                print('Black wins.')
                return
            
            elif black[i] < white[i]:
                print('White wins.')
                return
        print('Tie.')

while len(hands) != 0 and len(hands) == 10:
    for i in range(10):
        if i < 5:
            black_value.append(encode_card(hands[i]))
        else:
            white_value.append(encode_card(hands[i]))

    # 패를 정렬해두면 족보 판정을 훨씬 쉽게 할 수 있고, 같은 족보일 때 비교하기 위한 제일 높은 카드도 쉽게 찾을 수 있다.
    black_value.sort(reverse=True)
    white_value.sort(reverse=True)

    black_hands_score = get_hands_score(black_value)
    white_hands_score = get_hands_score(white_value)

    hands_compare(black_hands_score, white_hands_score)
    
    black_value.clear()
    white_value.clear()
    
    black_hands_score.clear()
    white_hands_score.clear()

    hands = input().split()