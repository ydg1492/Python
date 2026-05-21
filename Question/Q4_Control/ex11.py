# 문제11. 
# 다음과 같은 형식의 문장을 visited 변수에 저장되어 있다. 
# visited = '오늘 방문자 수는 350명이었고, 어제는 280명이었다.' 
# 1. 문장 안에서 숫자로 이루어진 부분(예: "350" , "280")을 직접 찾아 정수로 
# 변환하여 두 수의 차이를 출력 하시오. 
# 2. 오늘이 더 많으면 "증가", 적으면 "감소" 
# ※ 리스트 사용 없이 문자열 처리만으로 해결해야 함. 
# (hint: ‘명’자를 찾아서 그 앞의 숫자를 찾아냅니다. ‘ ‘공백문자를 찾아서 숫자의 길이 
# 계산) 

visited = "오늘 방문자 수는 350명이었고, 어제는 280명이었다."

visit1 = visited.find("350")
visit2 = visited.find("280")

today = int(visited[visit1:visit1+3])
yesterday = int(visited[visit2:visit2+3])


diff = today - yesterday

print("차이:", diff)

# 증가 / 감소 판단
if diff > 0:
    print("증가")
elif diff < 0:
    print("감소")
else:
    print("변화 없음")