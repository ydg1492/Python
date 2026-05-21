from csv import DictReader
import json

results = []

with open("Submit/scores.csv", "r", encoding="utf-8-sig") as file:
    reader = DictReader(file)

    for row in reader:
        name = row["이름"]

        korean = int(row["국어"])
        english = int(row["영어"])
        math = int(row["수학"])

        total = korean + english + math
        avg = total / 3

        results.append({
            "이름": name,
            "총점": total,
            "평균": round(avg, 2)
        })

print("현재 데이터검증:")
print(results)

print("JSON 저장 시작")

with open("Submit/result.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

print("JSON 저장 완료")
print(results)