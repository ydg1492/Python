import pandas as pd

df = pd.read_csv("Submit/scores.csv")

df.index = range(1, len(df) + 1)


pivot = pd.pivot_table(
    df,
    index="이름",
    values=["국어", "영어", "수학"],
    aggfunc="sum"
)


pivot["총점"] = pivot.sum(axis=1)
pivot["평균"] = pivot[["국어", "영어", "수학"]].mean(axis=1).round(2)


result = pivot[["총점", "평균"]].reset_index()

print(result.to_string(index=False))


result.to_csv("Submit/resultpivot.csv", index=False, encoding="utf-8-sig")