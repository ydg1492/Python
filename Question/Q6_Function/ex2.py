# 문제2. 
# 섭씨(Celsius)온도를 입력하면 화씨(Fahrenheit)온도를 반환하는 cel_to_fah라는 
# 이름의 
# 함수와 그 반대로 화씨 온도를 입력하면 섭씨 온도를 반환하는 fah_to_cel라는 이름의 
# 함수를 정의하고 이 두 함수를 호출하는 예제를 완성해 보자. 참고로 섭씨와 화씨간의 
# 온도변환의 공식은 다음과 같다. 
# Fah=1.8*Cel+32 

def cel_to_fah():
   Cel= int(input("섭씨온도 입력:"))
   Fah=1.8 *Cel+32
   print("화씨온도:",Fah)

cel_to_fah()

def fah_to_cel():
   Fah= int(input("화씨온도 입력:"))
   Cel=(Fah - 32) / 1.8
   print("섭씨온도:",Cel)

fah_to_cel()

# def cel_to_fah(cel):
#     return 1.8 * cel + 32


# def fah_to_cel(fah):
#     return (fah - 32) / 1.8


# celsius = 30
# fahrenheit = cel_to_fah(celsius)

# print("섭씨:", celsius)
# print("화씨:", fahrenheit)

# fah = 86
# cel = fah_to_cel(fah)

# print("화씨:", fah)
# print("섭씨:", cel)