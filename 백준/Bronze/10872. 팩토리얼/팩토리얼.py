n = int(input())

def Factorial(n):
    result = 1
    if n > 0:
        result = n * Factorial(n-1)
    return result

print(Factorial(n))