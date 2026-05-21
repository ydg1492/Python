# from datetime import date

# a_day = date(2026, 4, 29)
# today = date.today()

# diff = today - a_day

# print(f"{diff.days}일")
# print(f"개강일 부터: {diff.days}일 경과")

from datetime import date, datetime
import csv

today = date.today()

attendance = []

print("=== 출석 시스템 ===")

while True:
    name = input("이름 입력 (종료: q): ")

    if name == "q":
        break

    status = input("상태 (출석/지각/결석): ")

    attendance.append([name, str(today), status])


# CSV 저장
with open("attendance.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "날짜", "상태"])
    writer.writerows(attendance)

print("저장 완료!")
