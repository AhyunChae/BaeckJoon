def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

input_num = int(input())
print(fib(input_num))