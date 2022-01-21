def merge(left,right):
    l = 0
    r = 0
    merged_list = list()
    num_of_inversions = 0
    while l < len(left) or r < len(right):

        if l < len(left) and left[l] <= right[r]:
            merged_list.append(left[l])
            l +=1

        elif r < len(right):
            merged_list.append(right[r])
            num_of_inversions +=  len(left) - l
            r += 1

        if r >= len(right):
            merged_list += left[l:]
            break
        elif l >= len(left):
            merged_list += right[r:]
            break
    #print((merged_list, num_of_inversions))
    return (merged_list, num_of_inversions)

def merge_sort(unsorted_array):

    if len(unsorted_array) == 1: return unsorted_array,0

    else:

        midpoint = len(unsorted_array) // 2
        #print( merge_sort(unsorted_array[0:midpoint]))
        left_side,left_inv = merge_sort(unsorted_array[0:midpoint])
        right_side, right_inv = merge_sort(unsorted_array[midpoint:])
        merged_list, split_count = merge(left_side,right_side)
        return merged_list, split_count +left_inv+right_inv
array = [1,20,6,7,5,8,11,3]
print(merge_sort(array))
