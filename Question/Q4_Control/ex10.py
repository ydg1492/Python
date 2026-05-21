# 문제10. 
# 사용자로부터 파일명을 하나 입력받아 아래를 판단하세요. 
# 예) report_2025_final.csv 
# 1. 파일 이름에 "2025"가 들어 있으면 "올해 파일" 
# 2. "report"로 시작하면 "보고서 유형" 
# 3. ".csv"로 끝나면 "CSV 데이터 파일" 
# 위 조건 중 해당되는 것들을 모두 출력 (해당되는 것이 여러 개일 수 있음) 
# 출력 예) “올해 파일, 보고서 유형, CSV 데이터 파일” 
# (hint: .startswith(), .endswith(),in, 문자열 누적 결합연산으로 결과
#  만들어요.) 
 
filename = input("파일명을 입력하세요: ")

if "2025" in filename:
    print("올해 파일")

if filename.startswith("report"):
    print("보고서 유형")

if filename.endswith(".csv"):
    print("CSV 데이터 파일")