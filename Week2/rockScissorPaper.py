# 컴퓨터와 함께하는 가위바위보 게임
# 조건1 : 함수의 인자로는 나의 가위바위보 선택이 들어감
# 조건2 : 누가 무엇을 냈고, 누가 승리했는지 출력되어야 함

import random

def check_my():
  my = input('가위 바위 보 중에 하나를 입력해주세요: ')
  if my == "가위":
    my = 0
    print("나 : 가위")
  elif my == "바위":
    my = 1
    print("나 : 바위")
  elif my == "보":
    my = 2
    print("나 : 보")
  else:
    my = input("값을 잘못 입력했습니다. 다시 입력해주세요.\n")
    

def check_cmp():
  cmp = random.randint(0, 2)
  if cmp == 0:
    cmp = "가위"
    print("컴퓨터 : 가위")
  elif cmp == 1:
    cmp = "바위"
    print("컴퓨터 : 바위")
  elif cmp == 2:
    cmp = "보"
    print("컴퓨터 : 보")
  else:
    cmp = input("값을 잘못 입력했습니다. 다시 입력해주세요.\n")


def rsp(my, cmp):
  if my == cmp:
    print("비겼습니다.")
  elif my == 0 & cmp == 1:
    print("졌습니다.")
  elif my == 0 & cmp == 2:
    print("이겼습니다!")
  elif my == 1 & cmp == 0:
    print("이겼습니다!")
  elif my == 1 & cmp == 2:
    print("졌습니다.")
  elif my == 2 & cmp == 0:
    print("졌습니다.")
  elif my == 2 & cmp == 1:
    print("이겼습니다.")


my = check_my()
cmp = check_cmp()
rsp(my, cmp)
