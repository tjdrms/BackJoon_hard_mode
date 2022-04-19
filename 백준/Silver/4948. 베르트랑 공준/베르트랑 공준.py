num = []

for i in range(2, 246913):
    not_sosu = 0
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            not_sosu+=1
            break
    if not_sosu == 0:
        num.append(i)
        
while True:
    n = int(input())
    if n == 0:
        break
    sosu = 0
    
    for i in num:
        if n < i <= 2*n:
            sosu+=1
    print(sosu)