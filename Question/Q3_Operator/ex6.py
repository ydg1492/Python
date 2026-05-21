custom_money= int(input("손님한테 밥은 금액 입력"))
price= int(input("구입한 상품의 가격 입력"))

#부가세
tax = int(price * 0.1)
# 잔돈
change = custom_money - (price+tax)
print(f"받은 돈   : {custom_money}원")
print(f"상품 가격 : {price}원")
print()
print(f"부가세    : {tax}원")
print(f"잔돈      : {change}원")
