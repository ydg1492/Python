# 문제5. 
# 프로그램 사용자로부터 입력 받은 정수의 평균을 출력하는 프로그램을 작성하되 다음 두 
# 가지 조건을 만족시켜야 한다. - 먼저 몇 개의 정수를 입력할 것인지 프로그램 사용자에게 묻는다.  
# 그리고 그 수 만큼 정수를 입력 받는다. - 평균값은 소수점 이하까지 출력되도록 한다.
count = int(input("몇 개의 정수를 입력하시겠어요: "))

total = 0

for i in range(count):
    num = int(input("정수 입력: "))
    total += num

avg = total / count

print("평균:", avg)