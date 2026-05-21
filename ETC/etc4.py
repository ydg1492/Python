with open("Submit/scores.csv", 'r', encoding='UTF-8') as f:
    next(f)

    scores = {
        "국어": [],
        "영어": [],
        "수학": []
    }

    for i in f:
        row = i.strip().split(',')

        scores["국어"].append(int(row[1]))
        scores["영어"].append(int(row[2]))
        scores["수학"].append(int(row[3]))

for subject in scores:
    total = sum(scores[subject])
    avg = total / len(scores[subject])
    mx = max(scores[subject])
    mi = min(scores[subject])
    print(f"{subject} - 평균: {round(avg, 2)}, 최고점: {mx} , 최저점: {mi}")


