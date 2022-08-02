# 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수
# 소수: 1과 자기 자신만을 약수로 가지는 수

def count_prime_number(n, m):
    if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break


n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)