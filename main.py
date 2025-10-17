def find_median(arr):
    sorted_arr = sorted(arr)
    arr_length = len(sorted_arr)

    if arr_length % 2 == 1:
        return sorted_arr[arr_length // 2]

    else:
        midLeft = sorted_arr[(arr_length // 2) - 1]
        midRight = sorted_arr[arr_length // 2]
        return (midLeft + midRight) / 2


N = input("Введите числа через \" \":").split(' ')
arr = [int(x) for x in N]
result = find_median(arr)

print(arr)
print(result)
