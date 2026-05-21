# 문제 2. 
# 사용자로부터 정수형 숫자 하나를 입력받자. 이 입력된 숫자 만큼 사용자로 부터 
# 문자열을 입력받아 리스트에 저장하도록 해보자. 
# 입력된 문자열들이 잘 저장되어 있는지 확인하기 위해 배열의 각 요소들을 for in 
# 반복문으로 차례로 출력해보자.


count = int(input("입력할 문자열 개수를 입력하세요: "))
words = []
for i in range(count):
    text = input(f"{i+1}번째 문자열 입력: ")
    words.append(text)

print("\n저장된 문자열:")

for word in words:
    #print(word, end=',')
    print(", ".join(words))