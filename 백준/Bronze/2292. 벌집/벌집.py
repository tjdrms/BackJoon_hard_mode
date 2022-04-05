n=int(input())

room_count = 1
count = 1

while n > room_count:
    room_count += (6*count)
    count += 1
    
print(count)