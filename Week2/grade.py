# 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기
# 조건 : 이름과 점수, 학점 모두 출력해야 함

def calculate_grade(std_name, std_score):
    if std_score >= 95 :
        grade = "A+"
    elif std_score >= 90 :
        grade = "A"
    elif std_score >= 85 :
        grade = "B+"
    elif std_score >= 80 :
        grade = "B"
    elif std_score >= 75 :
        grade = "C+"
    elif std_score >= 70 :
        grade = "C"
    elif std_score >= 65 :
        grade = "D+"
    elif std_score >= 60 :
        grade = "D"
    else:
        grade = "F"
    return grade

std_name = input("이름을 입력해주세요 : ")
std_score = int(input("점수를 입력해주세요 : "))

print(f"학생이름 : {std_name}\n점수 : {std_score}")
print("학점 : ", calculate_grade(std_name, std_score))