# 문제10. 
# 구구단을 출력하되 짝수 단(2단, 4단, 6단, 8단)만 출력되도록 한다. 또한 2단은 
# 2*2까지, 
# 4단은 4*4까지, 6단은 6*6까지, 8단은 8*8까지만 출력되도록 해보자. 이를 해결하기  
# 위해 break와 continue문을 사용해보자. 
# ( break, continue를 안써도 프로그래밍은 가능하지만 연습하는 의미에서 적용해보세요. )
for dan in range(2, 10):

    # 홀수 단은 SKIP
    if dan % 2 != 0:
        continue

    for i in range(1, 10):

        # 짝수단까지만 출력
        if i > dan:
            break

        print(f"{dan} x {i} = {dan * i}")

    print()  # 단 사이에 줄바꿈