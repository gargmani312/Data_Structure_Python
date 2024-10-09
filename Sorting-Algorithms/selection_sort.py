def selection_sort(arr):
    '''
    params: list of integers
    returns: sorted list of integers
    '''    
    len_of_arr = len(arr)
    for i in range(len_of_arr):
        min_index = i
        for j in range(i+1, len_of_arr):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(selection_sort(arr))
