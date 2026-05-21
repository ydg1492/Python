#현재 시간(시,분,초)를 각각 정수형 변수에 입력받아 오늘 00시 00분 00초를 기준으로 몇 초가 흘렀는지를 계산하는 프로그램을 작성하시오. 

hour = int(input("시를 입력: "))
minute = int(input("분을 입력: "))
second = int(input("초를 입력: "))

#00시 00분 00초 기준으로 총 초 계산
#1시간 = 3600초, 1분 = 60초
total_second = (hour * 3600) + (minute * 60) + second

# 3. 결과 출력
print(f"입력시간: {hour}시 {minute}분 {second}초")
print(f"오늘 00시 00분 00초부터 {total_second}초가 흘렀습니다.")