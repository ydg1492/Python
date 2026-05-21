# 문제3. 
# 사용자로부터 정수 3개를 입력받아 정수형 변수 a, b, c 에 각각 저장한 후, 조건문을 
# 사용하여 이들 변수 중 가장 큰 값을 가진 변수의 값을 max라는 이름의 정수형 변수에 
# 대입하고 출력하는 프로그램을 작성하시오.
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))
num3 = int(input("세 번째 정수를 입력하세요: "))

if num1 > num2 and num1 > num3:
     max_value = num1

elif num2 > num1 and num2 > num3:
     max_value = num2

else:
     max_value = num3

print(f"가장 큰 값: { max_value }입니다.")