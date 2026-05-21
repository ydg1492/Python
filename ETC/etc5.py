# with open("Submit/scores.csv", 'r', encoding='UTF-8') as f:
#     next(f)

#     result_list = []

#     for row in f:
#         row = row.strip().split(',')

#         name = row[0]
#         korean = int(row[1])
#         english = int(row[2])
#         math = int(row[3])

#         total = korean + english + math
#         avg = total / 3

#         result_list.append({"이름": name,"총점": total,"평균": round(avg, 2)})

# print(result_list)

# with open("Submit/result.csv", "w", encoding="UTF-8") as f:
#     f.write("이름,총점,평균")  # 헤더

#     for r in result_list:
#         f.write(f"{r['이름']},{r['총점']},{r['평균']}")
        
# print("결과저장완료")

with open("Submit/scores.csv", 'r', encoding='UTF-8') as f:
    next(f)

    data = list(map(lambda row: row.strip().split(','), f))


result_list = list(map(lambda r: {
    "이름": r[0],
    "총점": int(r[1]) + int(r[2]) + int(r[3]),
    "평균": round((int(r[1]) + int(r[2]) + int(r[3])) / 3, 2)
}, data))


with open("Submit/result.csv", "w", encoding="UTF-8") as f:
    f.write("이름,총점,평균\n")  # 줄바꿈 필수

    list(map(lambda r: f.write(f"{r['이름']},{r['총점']},{r['평균']}\n"), result_list))

print(result_list)
print("결과저장완료")