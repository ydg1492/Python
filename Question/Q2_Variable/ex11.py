# numbers = list(map(int, input("숫자 여러 개 입력: ").split()))
# print("입력한 숫자들:", numbers)
# print("합계:", sum(numbers))

# user_id= input("아이디: ")
# user_pw= input("비밀번호: ")

# if user_id=="admin" and user_pw =="1234":
#     print("로그인 성공!")
# else:
#     print("아이디 또는 비밀번호가 틀렸습니다.")    



# def swap(a, b):
#     return b, a

# a = 5
# b = 9

# a, b = swap(a, b)

# print(a, b) 

# a = input("문자열 입력> ")
# b = input("문자열 입력> ")

# print(a, b)

# c = a
# a = b
# b = c

# print(a, b)

user_id= input("아이디 입력:")
user_pw= input("비밀번호 입력:")

if user_id=="admin" :
     print("관리자 로그인 성공!")
elif user_id=="user":
     print("사용자 로그인 성공")
elif user_id=="guset":
     print("게스트 로그인 성공.") 

while True:
  
   dan= int(input("몇단인지 입력:(0:종료)"))

   if dan == 0:
     break
   else:
       print("{}단.".format(dan))
       print("===================================")
       for i in range(1,10):
        print(dan, "*", i, "=", dan * i )      
       print("===================================")
