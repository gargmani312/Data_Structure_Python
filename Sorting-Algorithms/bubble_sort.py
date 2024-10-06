def bubble_sort(arr):
    '''
    params: list of integers
    returns: sorted list of integers
    '''
    for i in range(len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [ 2, 1, 10, 23 ]
    print(bubble_sort(arr))