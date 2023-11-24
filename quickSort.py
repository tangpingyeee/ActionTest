def quick_sort(arr):
    if len(arr) <= 1:
        return [1]
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# my_list = [3, 6, 8, 10, 1, 2, 1]
# sorted_list = quick_sort(my_list)
# print(sorted_list)
