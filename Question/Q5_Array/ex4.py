# 문제 4. 
# 첫번째 리스트 list1은 [10, 20, 30, 40, 50]의 정수형 요소값을 가지고 있다. 
# 두번째 리스트 list2은 [ 1, 2 , 3 , 4 , 5 ]의 정수형 요소값을 가지고 있다. 
# 세번째 리스트 list3의 요소값은 list1의 요소와 list2의 요소값을 차례로 덧셈한 
# 결과를 저장하도록 프로그래밍 해보자. 단 list2의 요소는 역순으로 더해지도록 하자. 
# 즉, list1의 0번요소와 list2의 4번요소를 더해서 list3의 0번요소에 대입하도록 
# 해야한다. 
# list3의 1번 요소에는 list1의 1번 요소와 list2의 3번 요소가 더해져야 한다는 
# 것이다. 
# 이렇게 list3의 요소값을 모두 대입하고 그 값을 차례대로 출력해보자. 
list1 = [10, 20, 30, 40, 50]
list2 = [1, 2, 3, 4, 5]

list2.reverse()

list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])

print(list3)
print()

list3[0]=(list1[0]+list2[4])
print(list3)
print()

list3[1]=(list1[1]+list2[3])
print(list3)


