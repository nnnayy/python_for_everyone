# 월급을 입력하면 연봉을 계산해주는 계산기
# 조건 : 세전 연봉과 세후 연봉을 함께 출력

def yearly_payment(salary):
    annual_salary = salary * 12
  
    if annual_salary <= 1200:
        tax = 0.06
    elif annual_salary <= 4600:
        tax = 0.15
    elif annual_salary <= 8800:
        tax = 0.24
    elif annual_salary <= 15000:
        tax = 0.35
    elif annual_salary <= 30000:
        tax = 0.38
    elif annual_salary <= 50000:
        tax = 0.4
    else:
        tax = 0.42

    print(f"세전 연봉 : {annual_salary}만원")
    print(f"세후 연봉 : {annual_salary * (1-tax)}만원")


salary = int(input("월급을 입력해주세요 : "))

yearly_payment(salary)