# 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기

def bus_fare(age, payment):
  if age < 8 :
    fare = "무료"
  elif age >= 8 and age < 14 :
    fare = "450원"
  elif age >= 14 and age < 20 and payment == "카드":
    fare = "720원"
  elif age >= 14 and age < 20 and payment == "현금":
    fare = "1000원"
  elif age >= 20 and age < 75 and payment == "카드":
    fare = "1200원"
  elif age >= 20 and age < 75 and payment == "현금":
    fare = "1300원"
  else:
    fare = "무료"
  return fare


age = int(input("나이를 입력해주세요 : "))
payment = input("지불유형을 입력해주세요 : ")

print(f"나이 : {age}\n지불유형 : {payment}")
print(f"버스요금 : {bus_fare(age, payment)}")