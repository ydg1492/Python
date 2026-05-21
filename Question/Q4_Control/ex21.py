# 문제9. 
# 사용자로부터 5개의 단어를 ,(콤마)를 구분자로 하여 입력받아, 그 중 문자 길이가 5 
# 이상인 단어만 출력하세요. (hint. 입력된 문자열은 1개임- 1개의 문자열안에 콤마가 
# 여러개인 것임. )
text = input("단어 입력 (콤마구분): ")

words = text.split(",")

for word in words:
    word = word.strip()  # 공백 제거
    if len(word) >= 5:
        print(word)