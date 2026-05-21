# import os

# print("현재 작업 경로:")
# print(os.getcwd())

# print()

# print("현재 파일 경로:")
# print(os.path.abspath(__file__))

# print()

# print("현재 파일 폴더:")
# print(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk

file_path = "Submit/scores.csv"

# CSV 읽기
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.read().strip().split("\n")

data = []

for line in lines:
    data.append(line.split(","))

root = tk.Tk()
root.title("CSV 점수 수정")
entries = []


for r, row in enumerate(data):
    row_entries = []
    for c, value in enumerate(row):
        e = tk.Entry(root, width=10)
        e.grid(row=r, column=c)
        e.insert(0, value)

        row_entries.append(e)
    entries.append(row_entries)

def save():
    new_data = []

    for row in entries:
        new_row = []
        for e in row:
            new_row.append(e.get())
        new_data.append(",".join(new_row))

    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_data))

    print("저장 완료!")

# 저장 버튼
btn = tk.Button(root, text="저장", command=save)
btn.grid(row=len(data), column=0, columnspan=len(data[0]), pady=10)
root.mainloop()