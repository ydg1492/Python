# def gugudan(start, end):
#     start, end = sorted([start, end])

#     for dan in range(start, end + 1):
#         print(f"\n== {dan}단 ==")
#         for i in range(1, 10):
#             print(f"{dan} x {i} = {dan * i:2}")  

# num1 = int(input("첫 번째 숫자 입력: "))
# num2 = int(input("두 번째 숫자 입력: "))
# gugudan(num1, num2)     

a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))

start, end = sorted([a, b])

list(map(
    lambda dan: print(
        f"\n== {dan}단 ==",
        "\n".join(map(lambda i: f"{dan} x {i} = {dan*i}", range(1, 10))),
        sep="\n"
    ),
    range(start, end + 1)
))

