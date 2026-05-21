# classes = []

# for i in range(3):
#     count = int(input(f"[{i+1}반] 인원 수 입력 : "))
#     scores = []

#     for j in range(count):
#         score = int(input(f"[{i+1}반 {j+1}번] : "))
#         scores.append(score)

#     classes.append(scores)

# print("\n===== 반별 성적 대시보드 =====\n")

# total_sum = 0
# total_count = 0

# best_avg = float("-inf")
# best_class = 0

# for i, scores in enumerate(classes):
#     class_sum = sum(scores)
#     class_avg = class_sum / len(scores)

#     total_sum += class_sum
#     total_count += len(scores)

#     print(f"[{i+1}반]")
#     print(f"학생 수: {len(scores)}")
#     print(f"점수: {scores}")
#     print(f"평균: {class_avg:.2f}")
#     print(f"최고점: {max(scores)}")
#     print(f"최저점: {min(scores)}")
#     print("-" * 30)

#     if class_avg > best_avg:
#         best_avg = class_avg
#         best_class = i + 1

# print(f"전체 평균: {total_sum / total_count:.2f}")
# print(f"최고 반: {best_class}반")

classes = {}

for i in range(3):
    count = int(input(f"[{i+1}반] 인원 수 입력 : "))
    scores = []

    for j in range(count):
        score = int(input(f"[{i+1}반 {j+1}번] : "))
        scores.append(score)

    classes[f"{i+1}반"] = scores


print("\n===== 반별 성적 대시보드 =====\n")

total_sum = 0
total_count = 0

best_avg = float("-inf")
best_class = ""

for class_name, scores in classes.items():

    class_sum = sum(scores)
    class_avg = class_sum / len(scores)

    total_sum += class_sum
    total_count += len(scores)

    class_max = max(scores)
    class_min = min(scores)

    print(f"[{class_name}]")
    print(f"학생 수: {len(scores)}")
    print(f"점수: {scores}")
    print(f"평균: {class_avg:.2f}")
    print(f"최고점: {class_max}")
    print(f"최저점: {class_min}")
    print("-" * 30)

    if class_avg > best_avg:
        best_avg = class_avg
        best_class = class_name


print(f"전체 평균: {total_sum / total_count:.2f}")
print(f"최고 반: {best_class}")