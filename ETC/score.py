# 문제 10. 
# 어느 교육원의 Python Programming 성적을 저장하는 프로그램을 만들어보다. 
# 교육원의 Python Programming은 3개 반으로 운영되고 있다. 단, 각 반의 인원수는 
# 서로 다를 수 있다. 
# 프로그램 사용자가 3개반의 성적을 입력하기 전에 해당 반의 인원수를 입력할 수 있도록 
# 하고 그 인원수 만큼 성적을 넣으면 다음 반의 인원수를 입력하는 방식으로 3개반의 모든 
# 성적을 입력해보자.  
# 모든 성적 입력이 끝났으면 그 값들을 출력해보고 각 반의 평균도 같이 계산되도록 
# 해보자.

# [1반] 인원 수 입력 : 3 
# [1반 1번] : 80 
# [1반 2번] : 70 
# [1반 3번] : 60 
# [2반] 인원 수 입력 : 4 
# [2반 1번] : 90 
# [2반 2번] : 80 
# [2반 3번] : 80 
# [2반 4번] : 60 
# [3반] 인원 수 입력 : 5 
# [3반 1번] : 90 
# [3반 2번] : 80 
# [3반 3번] : 70 
# [3반 4번] : 40 
# [3반 5번] : 60 
# --- Python Programming 성적표 ---- 
# [1반]  80  70  60   [평균 : 70.0]             
# [2반]  90  80  80  60   [평균 : 77.5] 
# [3반]  90  80  70  40  60  [평균 : 68.0]
# ----------------------- 
# 전체평균 :  71.67 
# 최우수 반 : [2반]  

classes= {}

for i in range(3):
    count = int(input(f"{i+1}반 인원수 입력:")) #반인원수 입력
    scores = []
    for j in range(count):
        score = int(input(f"[{i+1}반 {j+1}번] : ")) #반별인원수 성적입력
        scores.append(score)

    classes[f"{i+1}반"] = scores #딕셔너리 데이터추가

print("\n---- Python Programming 성적표 ----")

total_sum = 0 #전체반성적 초기화
total_count = 0 #전체반인원 초기화
best_avg = float('-inf') #최고성적반평균 초기화(최대값 찾기용 초기 기준값)
best_class = ""          #최고성적반 초기화

for class_name, scores in classes.items():

    class_sum = sum(scores)  
    class_count = len(scores)

    class_avg = class_sum / class_count if class_count > 0 else 0

    total_sum += class_sum
    total_count += class_count

    print(f"[{class_name}] {' '.join(map(str, scores))} [평균 : {class_avg:.1f}]")

    if class_avg > best_avg:
        best_avg = class_avg
        best_class = class_name

print("-----------------------")

total_avg = total_sum / total_count if total_count > 0 else 0
print(f"전체평균 : {total_avg:.2f}")
print(f"최우수 반 : [{best_class}]")
