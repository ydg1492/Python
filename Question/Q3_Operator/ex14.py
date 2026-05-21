mail_address= input("메일 주소 입력(@포함):")


separate = mail_address.split("@")

user_name = separate[0]
mail_server_name = separate[1]

print("입력된 메일주소명 :", user_name)
print("메일서버 이름 :", mail_server_name)