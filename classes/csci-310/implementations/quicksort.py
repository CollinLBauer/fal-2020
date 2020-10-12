
def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)

def quicksort_helper(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quicksort_helper(arr, low, p_index-1)
        quicksort_helper(arr, p_index+1, high)

def partition(arr, low, high):
    #print(low, high, arr)
    p_index = high

    i = low - 1
    for j in range(low, high + 1):
        if arr[j] < arr[p_index]:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i+1, p_index)

    return i+1

# just swap two elements
# technically not needed for python because simultaneous assignment but bite me
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def test():
    from random import randint
    MIN = -50
    MAX = 50
    
    test_list = []
    for i in range(10):
        test_list.append(randint(MIN, MAX))

    control_list = test_list.copy()

    print(test_list)

    quicksort(test_list)
    control_list.sort()

    print(test_list == control_list)

if __name__ == "__main__":
    test()