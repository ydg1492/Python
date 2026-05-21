# 문제1. 
# 세 개의 정수를 인자로 전달받아서 그 중 가장 큰 수를 반환하는 함수와 가장 작은 수를 
# 반환하는 함수를 정의해 보자. 그리고 이 함수를 호출하는 프로그램도 작성해보자. 
# [파이썬 내장함수 min, max를 직접 만들어 보아요. 함수의 이름은 각자 적절한 식별자를 
# 명명하시오.]
numbers= []
def return_number():

    for i in range(3):
     num=int(input(f"{i+1}번째 정수를 입력: "))
     numbers.append(num) 
    
return_number()
print("최대값:",max(numbers))
print("최소값:",min(numbers))


# def aaa():
#     num1=int(input("1번째 정수를 입력: "))
#     num2=int(input("2번째 정수를 입력: "))
#     num3=int(input("3번째 정수를 입력: "))
    
#     print("최대값:",max(num1, num2, num3))
#     print("최소값:",min(num1, num2, num3))
   
# aaa()

