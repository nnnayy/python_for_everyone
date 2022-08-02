# 가위바위보 업그레이드 버젼
# 조건1 : 게임을 몇 판 진행할 것인지 입력 받아주기
# 조건2 : 0,1,2,"가위","바위","보" 이외에 다른 입력을 받으면 재입력 받기
# 조건3 : 게임종료 후 나와 컴퓨터의 총 전적 출력하기

import random

def rsp_advanced(games):
    win = 0
    lose = 0
    draw = 0

    for i in range(1, games + 1):
        my = input('가위 바위 보 : ')

        if my == "가위" or my == "0":
            my = 0
            print("나 : 가위")
        if my == "바위" or my == "1":
            my = 1
            print("나 : 바위")
        if my == "보" or my == "2":
            my = 2
            print("나 : 보")

        cmp = random.randint(0, 2)

        if cmp == 0:
            print("컴퓨터 : 가위")
        elif cmp == 1:
            print("컴퓨터 : 바위")
        elif cmp == 2:
            print("컴퓨터 : 보")
        
        if (my == 0) & (cmp == 1):
            print(f"{i}번째 판 컴퓨터의 승리!\n")
            lose += 1
        if (my == 0) & (cmp == 2):
            print(f"{i}번째 판 나의 승리!\n")
            win += 1
        if (my == 1) & (cmp == 0):
            print(f"{i}번째 판 나의 승리!\n")
            win += 1
        if (my == 1) & (cmp == 2):
            print(f"{i}번째 판 컴퓨터의 승리!\n")
            lose += 1
        if (my == 2) & (cmp == 0):
            print(f"{i}번째 판 컴퓨터의 승리!\n")
            lose += 1
        if (my == 2) & (cmp == 1):
            print(f"{i}번째 판 나의 승리!\n")
            win += 1
        if (my == cmp):
            print(f"{i}번째 판 비겼습니다!\n")
            draw += 1

        if i == games:
            print(f"나의 전적: {win}승 {draw}무 {lose}패")
            print(f"컴퓨터의 전적: {lose}승 {draw}무 {win}패")


games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)