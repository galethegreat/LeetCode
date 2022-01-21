def partition(array, left, right):
    pivot = left
    pivot_value = array[pivot]

    i = left + 1
    j = left + 1
    
    while j < right:
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1

        j += 1

    array[left], array[i-1] =  array[i-1], array[left]

    return i - 1

def quick_sort(unsorted_array,left, right):

    if left < right:
        pivot = left
        pivot_split_index = partition(unsorted_array, left, right)
        quick_sort(unsorted_array, left, pivot_split_index-1)
        quick_sort(unsorted_array, pivot_split_index +1, right)

array = [5,10,3,8,4,0]
quick_sort(array,0, len(array))
print(array)
