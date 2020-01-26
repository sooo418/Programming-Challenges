chess_len = 8
chess = [[],[],[],[],[],[],[],[]]

# 대 소문자 변환 함수
def switch_case(c):
    if c == '.':
        pass
    else:
        if c <= 'Z':
            c = chr(ord(c) + ord('a') - ord('A'))
        else:
            c = chr(ord(c) + ord('A') - ord('a'))
    return c

# 체스판 검은말에서 흰말로 교체해주는 함수
def turn_upside_down():
    global chess, chess_len
    for i in range(chess_len // 2):
        for j in range(chess_len):
            temp = chess[i][j]
            chess[i][j] = switch_case(chess[7-i][7-j])
            chess[7-i][7-j] = switch_case(temp)

# 좌표값을 변환시키면서 해당 위치에 찾는 말이 체스말이 있는지 체크하는 함수
def look_for_piece(piece, istart, jstart, di, dj):
    global chess, chess_len
    i = istart + di
    j = jstart + dj
    while i >= 0 and i <= 7 and j >= 0 and j <= 7 and chess[i][j] == '.':
        i += di
        j += dj
    return i >= 0 and i <= 7 and j >= 0 and j <= 7 and chess[i][j] == piece

# 킹이 체크상태인지 검사하는 함수
def king_in_check():
    global chess, chess_len
    king_i = 0
    king_j = 0

    # 킹의 위치를 찾아 king_i와 king_j에 저장한다
    for i in range(chess_len):
        for j in range(chess_len):
            if chess[i][j] == 'k':
                king_i = i
                king_j = j
                break
    
    # 폰 Pawn
    if (king_i <= 6 and king_j >= 1 and chess[king_i+1][king_j-1] == 'P') or \
        (king_i <= 6 and king_j <= 6 and chess[king_i+1][king_j+1] == 'P'):
        return True
    
    # 나이트 Knight
    if (king_i >= 2 and king_j >= 1 and chess[king_i-2][king_j-1] == 'N') or \
        (king_i >= 1 and king_j >= 2 and chess[king_i-1][king_j-2] == 'N') or \
        (king_i >= 2 and king_j <= 6 and chess[king_i-2][king_j+1] == 'N') or \
        (king_i >= 1 and king_j <= 5 and chess[king_i-1][king_j+2] == 'N') or \
        (king_i <= 6 and king_j >= 2 and chess[king_i+1][king_j-2] == 'N') or \
        (king_i <= 5 and king_j >= 1 and chess[king_i+2][king_j-1] == 'N') or \
        (king_i <= 6 and king_j <= 5 and chess[king_i+1][king_j+2] == 'N') or \
        (king_i <= 5 and king_j <= 6 and chess[king_i+2][king_j+1] == 'N'):
        return True
    
    # 비숍 Bishop
    if look_for_piece('B', king_i, king_j, -1, -1) or \
        look_for_piece('B', king_i, king_j, -1, 1) or \
        look_for_piece('B', king_i, king_j, 1, -1) or \
        look_for_piece('B', king_i, king_j, 1, 1):
        return True
        
    # 룩 Rook
    if look_for_piece('R', king_i, king_j, -1, 0) or \
        look_for_piece('R', king_i, king_j, 1, 0) or \
        look_for_piece('R', king_i, king_j, 0, -1) or \
        look_for_piece('R', king_i, king_j, 0, 1):
        return True

    # 퀸 Queen
    if look_for_piece('Q', king_i, king_j, -1, -1) or \
        look_for_piece('Q', king_i, king_j, -1, 1) or \
        look_for_piece('Q', king_i, king_j, 1, -1) or \
        look_for_piece('Q', king_i, king_j, 1, 1) or \
        look_for_piece('Q', king_i, king_j, -1, 0) or \
        look_for_piece('Q', king_i, king_j, 1, 0) or \
        look_for_piece('Q', king_i, king_j, 0, -1) or \
        look_for_piece('Q', king_i, king_j, 0, 1):
        return True

    # 킹 king
    for i in range(0 if king_i - 1 < 0 else king_i - 1, 7 if king_i + 1 > 7 else king_i + 1):
        for j in range(0 if king_j - 1 < 0 else king_j - 1, 7 if king_j + 1 > 7 else king_j + 1):
            if chess[i][j] == 'K':
                return True
    
    # 검사를 모두 통과하면 킹 안전
    return False

count = 0
while True:
    empty_board = 0
    # 체스판 생성
    try:
        for i in range(chess_len):
            row = input()
            if len(row) != 8:
                raise Exception('len(row) != 8')
            for j in range(chess_len):
                chess[i].append(row[j])
    except Exception as e:
        print("8자리를 맞혀서 입력해주세요..")
        print(e)
        
    
    for i in range(chess_len):
        if chess[i] != '........':
            empty_board = 1
            count += 1
            break

    if empty_board == 0:
        break

    print('Game #', end='')
    print(count, end='')

    if king_in_check():
        print(': black king is in check')
    else:
        turn_upside_down()
        if king_in_check():
            print(': white king is in check')
        else:
            print(': no king is in check')
    
    chess = [[],[],[],[],[],[],[],[]]