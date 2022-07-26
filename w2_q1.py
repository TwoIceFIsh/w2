import random

game_board = ['가위', '바위', '보']


def game_rule(my_select: int, com_select: int):
    input_list = [game_board[my_select], game_board[com_select]]

    if '가위' in input_list and '바위' in input_list:
        flag = '바위'
    elif '가위' in input_list and '보' in input_list:
        flag = '가위'
    elif '바위' in input_list and '보' in input_list:
        flag = '보'
    else:
        return '비김'

    if flag == game_board[my_select]:
        return "사용자 승!"
    else:
        return "컴퓨터 승!"


while True:
    # 1. 사용자 입력
    print('컴퓨터와 가위바위보를 해볼까요? 내고싶은 유형의 숫자를 골라주세요!')

    try:
        my_select = int(input(f'(가위(0) 바위(1) 보(2)) > '))
        if my_select not in range(3):
            print('0,1,2 중에서 입력해 주세요.')
            continue
    except ValueError:
        print('숫자를 입력해 주세요.')
        continue

    com_select = random.randint(0, 2)

    # 2. 사용자 및 컴퓨터 비교
    result = game_rule(my_select=my_select, com_select=com_select)

    # 3. 결과 출력
    print(f'[결과] {result} (나: {game_board[my_select]} / 컴퓨터: {game_board[com_select]})')
