# 문제 1. 
# 빈 리스트(요소가 없는 리스트)를 만들고 프로그램 사용자로부터 총 5개의 정수를 입력 
# 받아 리스트에 추가해보자.  
# 그리고 입력이 끝나면 다음의 내용을 출력하도록 예제를 작성해보자. - 입력된 정수 중에서 최대값 - 입력된 정수 중에서 최소값 - 입력된 정수의 총 합 
numbers= []
for i in range(5):
    num=int(input(f"{i+1}번째 정수를 입력: "))
    numbers.append(num) 
print("최대값:",max(numbers))
print("최소값:",min(numbers))
print("총합:",sum(numbers))