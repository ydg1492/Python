numbers= list(range(1,10+1))

print("홀수만 추출하기")
print(list(filter(lambda n:n%2 !=0, numbers)))
print()

print("#3이상, 7미만 추출하기")
print(list(filter(lambda n:3<= n <7, numbers)))
print()


print("#제곱해서 50미만 출력하기")
print(list(filter(lambda n:n**2<50, numbers)))
print()

numbers =[1,2,3,4,5,6]
print("::".join(map(str,numbers)))

import random

def generate_lotto():
    try:
        # 1. 사용자로부터 생성할 세트 수 입력받기
        count = int(input("생성할 로또 번호 세트 수를 입력하세요: "))
        
        print(f"\n--- {count}개의 로또 번호를 추출합니다 ---")
        
        for i in range(1, count + 1):
            # 2. 1~45 범위 내 중복 없이 6개 추출 (random.sample 사용)
            lotto_numbers = random.sample(range(1, 46), 6)
            # 3. 보기 좋게 오름차순 정렬
            lotto_numbers.sort()
            
            print(f"{i}세트 : {lotto_numbers}")
            
    except ValueError:
        print("올바른 숫자를 입력해 주세요.")

# 함수 실행
generate_lotto()

