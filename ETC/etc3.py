import pandas as pd

class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def total(self):
        return self.korean + self.english + self.math

    def average(self):
        return round(self.total() / 3, 2)

    def to_dict(self):
        return {
            "이름": self.name,
            "국어": self.korean,
            "영어": self.english,
            "수학": self.math,
            "총점": self.total(),
            "평균": self.average()
        }

students = [
    Student("김철수", 85, 90, 78),
    Student("이영희", 92, 88, 95),
    Student("박민수", 76, 80, 72),
    Student("최수지", 89, 94, 91),
    Student("정우성", 95, 85, 97),
    Student("한가은", 88, 92, 84),
    Student("오상민", 79, 75, 89),
    Student("윤지호", 91, 89, 87)
]


data = [student.to_dict() for student in students]

df = pd.DataFrame(data)


df.index = range(1, len(df) + 1)

print(df.to_string(index=False))

df.to_csv("Submit/result.csv", index=False, encoding="utf-8-sig")

print("CSV 파일 저장 완료!")