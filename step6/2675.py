T=int(input())

for i in range(T):
    r,s=input().split()
    text=''
    for i in s:
        text += int(r)*i
    print(text)
