n = int(input())

fans = list(map(int, input().split()))

fans.sort() 

current_time = 0
waiting = 0

for time in fans:
    current_time += time
    waiting += current_time  

print(waiting)
