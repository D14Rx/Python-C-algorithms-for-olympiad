a = int(input())

b = int(input())

n = int(input())

cost_rides = a * n

if cost_rides < b:
    print(cost_rides)
else:
    print(b)