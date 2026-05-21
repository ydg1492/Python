# 문제12. 
# 사용자로부터 하나의 문장을 입력받아 다음 기준에 따라 문장의 “유형”을 판단하세요. 
# 규칙: - 감탄사 "!" 로 끝나면 → "감탄 문장" - 물음표 "?" 로 끝나면 → "의문 문장" - 문장 길이가 30자 이상이면 → "긴 문장" - 문장에 숫자가 하나라도 포함되어 있으면 → "숫자 포함 문장" 
# 위 조건 중 해당되는 모든 유형을 출력하세요. 
# 예) 
# 입력: "Python is amazing! 123" 
# 출력: "감탄 문장, 긴 문장, 숫자 포함 문장" 
# [ hint: 문자열 끝 글자 확인, in, .replace() – 비효율적인 반복 작업이
#  필요합니다. ] 
text = input("문장을 입력하세요: ")

result = ""

# 1. 감탄 문장
if text.endswith("!"):
    result += "감탄 문장"

# 2. 의문 문장
if text.endswith("?"):
    if result:
        result += ", "
    result += "의문 문장"

# 3. 긴 문장
if len(text) >= 30:
    if result:
        result += ", "
    result += "긴 문장"

# 4. 숫자 포함 여부
for i in "0123456789":
    if i in text:
        if result:
            result += ", "
        result += "숫자 포함 문장"
        break

print(result)