# 문제9.  
# 사용자로부터 정수 3개를 입력받아 아래를 수행하세요. 
# 1. 세 수 중 가장 큰 값 출력 
# 2. 세 수의 평균 계산 
# 3. 평균이 70 이상이면 "통과", 아니면 "불합격" 출력 
# 4. 평균이 정수인지 실수인지 판단하여 "정수 평균" 또는 "실수 평균" 출력 
# (힌트: float은 소수점 아래가 있어요. 즉. 나눗셈의 나머지값이 있어요.  )
num1 = int(input("첫 번째 정수 입력: "))
num2 = int(input("두 번째 정수 입력: "))
num3 = int(input("세 번째 정수 입력: "))

if num1 > num2 and num1 > num3:
    max_value = num1

elif num2 > num1 and num2 > num3:
    max_value = num2

else:
    max_value = num3

print(f"가장 큰 값: {max_value}입니다.")


avg = (num1 + num2 + num3) / 3
print(f"평균: {avg:.2f}")


if avg >= 70:
    print("통과")
else:
    print("불합격")

if avg == int(avg):
    print("정수 평균")
else:
    print("실수 평균")
