# 한국 나이를 미국 나이로 변환하는 프로그램

korean_age = int(input("사용자의 한국 나이를 입력해주세요 : "))
birthday = int(input("생일이 지났나요?\n(지났으면 0, 아닌 경우 -1을 입력해주세요) : "))

if birthday == 0:
     us_age = korean_age-1
else:
     us_age = korean_age-2

print(f"사용자의 한국 나이{korean_age}는 미국 나이로 {us_age}입니다")