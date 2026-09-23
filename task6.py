n = int(input())

price = list(map(int, input().split()))

current_price = 0
min_price = price[0]
max_occupation = 0

for maximum in price:

    max_occupation = max(max_occupation, maximum - min_price) 
    min_price = min(min_price, maximum)

print(max_occupation)