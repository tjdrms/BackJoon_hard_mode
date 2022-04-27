n = int(input())

for _ in range(n):
    data = input()
    brackets = list(data)
    sum = 0
    
    for i in brackets:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
   
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")