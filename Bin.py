def binary_search(array, user_input, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if user_input == array[mid]:
        return mid

    if user_input < array[mid]:
        return binary_search(array, user_input, low, mid-1)
    else:
        return binary_search(array, user_input, mid+1, high)

    if low > high:
        return -1

    if len(array) == 1:
        if user_input == array[mid]:
            return mid
        else:
            return -1

user_input = int(input("Enter "))
array = []
for i in range(0, 100, 3):
    array.append(i)

print(binary_search(array,user_input,0,len(array)))



