n3 = int(input())

digits = [int (d)for d in str(n3)]

print(digits)

if n3 >  999:
    print("ERROR: more than 3 digits in number!!!")
else:
    print("List of numbers: {digits}") 