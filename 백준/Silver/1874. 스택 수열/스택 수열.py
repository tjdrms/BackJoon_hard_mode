n = int(input())
stack = []
pm = []
count = 1
temp = True

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        pm.append("+")
        count+=1
    if stack[-1] == num:
        stack.pop()
        pm.append("-")
    else:
        temp = False
if temp == False:
    print("NO")
else:
    for i in pm:
        print(i)