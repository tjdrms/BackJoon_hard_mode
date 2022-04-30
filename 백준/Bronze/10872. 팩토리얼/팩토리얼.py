n = int(input())

def Factorial(num):
    result = 1
    if num > 0:
        result = num * Factorial(num-1)
    return result

print(Factorial(n))