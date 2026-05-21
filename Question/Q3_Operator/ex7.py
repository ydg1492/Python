x1 = int(input("좌 상단의 x 좌표 : "))
y1 = int(input("좌 상단의 y 좌표 : "))
x2 = int(input("우 하단의 x 좌표 : "))
y2 = int(input("우 하단의 y 좌표 : "))

# 직사각형의 가로와 세로 길이 계산
width = x2 - x1
height = y2 - y1

# 넓이 계산 (가로 x 세로)
area = width * height

# 결과 출력
print(f"두 점이 이루는 직사각형의 넓이는 {area}입니다.")