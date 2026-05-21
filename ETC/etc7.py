with open("Submit/scores.csv", "r", encoding="UTF-8") as f:
    data = f.read()
    lines = data.splitlines()

korea_scores = []
eng_scores = []
math_scores = []

for line in lines[1:]:
    cols = line.split(",")
    korea_scores.append(int(cols[1]))
    eng_scores.append(int(cols[2]))
    math_scores.append(int(cols[3]))

korea_avg = sum(korea_scores) / len(korea_scores)
korea_avg = round(korea_avg,2)


eng_avg = sum(eng_scores) / len(eng_scores)
eng_avg = round(eng_avg,2)


math_avg = sum(math_scores) / len(math_scores)
math_avg = round(math_avg,2)

print("국어- 평균:", korea_avg, "최고점:", max(korea_scores), "최저점:", min(korea_scores) )
print("영어- 평균:", eng_avg, "최고점:", max(eng_scores), "최저점:", min(eng_scores) )
print("수학- 평균:", math_avg, "최고점:", max(math_scores), "최저점:", min(math_scores) )