from csv import DictReader
import json

subjects = {"국어": [], "영어": [], "수학": []}

with open("Submit/scores.csv", "r", encoding="utf-8") as file:
    reader = DictReader(file)

    for row in reader:
        for subject in subjects:
            subjects[subject].append(int(row[subject]))

# 과목별 통계 계산해서 JSON 구조로 만들기
result = {}

for subject, scores in subjects.items():
    result[subject] = {
        "평균": round(sum(scores) / len(scores), 2),
        "최고점": max(scores),
        "최저점": min(scores)
    }

# JSON 출력
print(json.dumps(result, ensure_ascii=False, indent=4))