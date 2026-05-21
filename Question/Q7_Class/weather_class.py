import pandas as pd


class MonthWeather:
    def __init__(self, month, avg_temp, max_temp, min_temp, rainfall, humi):
        self.month = month
        self.avg_temp = avg_temp
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.rainfall = rainfall
        self.humi = humi
 
    def dict(self):
        return {
            "월": self.month,
            "평균기온(℃)": self.avg_temp,
            "최고기온(℃)": self.max_temp,
            "최저기온(℃)": self.min_temp,
            "강수량(mm)": self.rainfall,
            "습도(%)": self.humi
        }


df = pd.read_excel("Question/Q7_Class/seoul_weather_2026.xlsx")



df.columns = df.columns.str.strip()


weather_list = []

for row in df.itertuples(index=False):

    weather = MonthWeather(
        row[0],  # month
        row[1],  # avg_temp
        row[2],  # max_temp
        row[3],  # min_temp
        row[4],  # rainfall
        row[5]   # humi
    )

    weather_list.append(weather)


df_result = pd.DataFrame([w.dict() for w in weather_list])

print(df_result.to_string(index=False))

