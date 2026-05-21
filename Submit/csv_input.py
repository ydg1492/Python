#import csv as c #csv모듈선언
from csv import DictReader

subjects = {"국어": [], "영어": [], "수학": [] } #과목딕셔너리

with open("Submit/scores.csv", "r", encoding="utf-8") as file: #csv읽어오기
    reader = DictReader(file)

    for row in reader:
        for subject in subjects:
            subjects[subject].append(int(row[subject]))

print("[과목별 통계]")

for subject, scores in subjects.items(): #딕셔너리 키,값을 뽑아내기
    print(f"{subject} - 평균: {sum(scores)/len(scores):.2f}",f"최고점: {max(scores)}", f"최저점: {min(scores)}")
    

# #JSON으로 데이터출력
# import json

# subjects = {"국어": [], "영어": [], "수학": []}

# with open("Submit/scores.csv", "r", encoding="utf-8") as file:
#     reader = DictReader(file)

#     for row in reader:
#         for subject in subjects:
#             subjects[subject].append(int(row[subject]))

# #JSON
# result = {}

# for subject, scores in subjects.items():
#     result[subject] = {
#         "평균": round(sum(scores) / len(scores), 2),
#         "최고점": max(scores),
#         "최저점": min(scores)
#     }

# # JSON 출력
# print(json.dumps(result, ensure_ascii=False, indent=4))
  