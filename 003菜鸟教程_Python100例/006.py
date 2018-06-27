# 题目：斐波那契数列。
def Fibonacci_Yield_tool(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1
def Fibonacci_Yield(n):
    return list(Fibonacci_Yield_tool(n))