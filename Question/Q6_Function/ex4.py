# def fib(n):
#     if n == 0:
#         return 0
    
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# def fibonacci(count):
#     for i in range(count):
#         print(fib(i), end=' ')
      

# num = int(input("출력할 개수 입력: "))
# fibonacci(num)

def fibonacci(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    print(", ".join(map(str, result)))


num = int(input("출력할 개수 입력: "))
fibonacci(num)