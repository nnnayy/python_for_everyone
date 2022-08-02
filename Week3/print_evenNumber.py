# 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수 
# 중앙값도 함께 출력
# 단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력
# 중앙값: 정중앙에 있는 값
# 특정 두 숫자 사이의 수들을 리스트로 만드는 법

def find_even_number(n, m):
    numbers = [i for i in range(n, m+1)]

    for num in range(numbers):
        if num % 2 == 0 & n + m / 2 == 0:
            print(f"{num} 짝수")
            print(f"{n + m / 2} 중앙값")


n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))

find_even_number(n, m)
