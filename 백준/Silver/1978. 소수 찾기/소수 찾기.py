n = int(input())
min = map(int, input().split())
count = 0

for i in min:
    if i==1:
        continue
    error = 0
    for j in range(2, i):
        if i%j == 0:
            error += 1
    if error == 0:
        count += 1
print(count)