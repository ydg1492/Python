# 문제 3. 
# 아래와 같이 학생들의 성적을 받아서 score_list 라는 이름의 리스트에 저장하고, 
# 평균을 구하는 프로그램을 작성해보자. (평균은 소수점 2자리까지만 표시) 
# 단, 입력값이 0~100 사이가 아니면 다시입력하도록 하시오.  
# 실행결과 예시) 
# 학생의 수를 입력하시오 : 2 
# 학생 1의 성적을 입력하세요 : 20 
# 학생 2의 성적을 입력하세요 : 110 
# 잘못된 성적입니다. 다시 입력하시오. 
# 학생 2의 성적을 입력하세요 : 30 
# —-------------------- 
# 학생 1의 성적 : 20 
# 학생 2의 성적 : 30 
# —-------------------- 
# 성적 평균은 25.00 입니다. 

count = int(input("학생의 수를 입력하시오 : "))

score_list = [] #빈 학생성적리스트



for i in range(count):

    while True:
        score = int(input(f"학생 {i+1}의 성적을 입력하세요 : "))

        if 0 <= score <= 100:
            score_list.append(score)
            break
        else:
            print("잘못된 성적입니다. 다시 입력하시오.")


print("-" * 20)

for i in range(count):
    print(f"학생 {i+1}의 성적 : {score_list[i]}")

print("-" * 20)

avg = sum(score_list) / count

print(f"성적 평균은 {avg:.2f} 입니다.")