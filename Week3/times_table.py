# 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수
# 조건1 : 홀수 번째만 출력하기
# 조건2 : 값이 50 이하인 것만 출력하기

def gugudan(num):
    print(f'{num} 단')
    
    for i in range(1, 10):
      if (i % 2 != 0) & (num * i < 40) :
        print(f'{num} X {i} = {num*i}')
    
number = int(input("몇 단? : "))
gugudan(number)