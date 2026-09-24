def binary(arr, item):
    low = 0 #hachalni element
    high = len(arr) - 1 #posledni element

    while low <= high:
        mid = (low + high) // 2 #delim na polovinu
        guess = arr[mid] 
        if guess == item:
            return mid

        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

list = [1,2,3,4,5,6,7,8,9,10]

print(binary(list, 6))
print(binary(list, 0))
print(binary(list, -9))