# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
if __name__ == '__main__':
    pass


def exchange(L, pos1, pos2):
    L[pos1], L[pos2] = L[pos2], L[pos1]


def new_partition(L: list, low: int, high: int):
    e = L[high]
    i = low - 1
    for j in range(low, high):
        if L[j] <= e:
            i = i + 1
            exchange(L, i, j)
    exchange(L, i + 1, high)
    first_list_end = handle_duplicates(i, L, low, e)
    return i + 1, first_list_end


# The main function that implements QuickSort
def new_quick_sort(low, high, List):
    if low < high:
        # p is partitioning index, array[p]
        # is at right place
        k, first_list_end = new_partition(List, low, high)

        # Sort elements before partition
        # and after partition
        new_quick_sort(low, first_list_end, List)
        new_quick_sort(k + 1, high, List)


def handle_duplicates(i, L: list, low, e):
    swap_index = i
    for k in range(low, i + 1):
        if swap_index <= k:
            break
        if L[k] == e:
            if L[swap_index] == e:
                swap_index = swap_index - 1
            exchange(L, swap_index, k)
            swap_index = swap_index - 1
    return swap_index


# The main function that implements QuickSort
def quick_sort(low, high, List):
    if low < high:
        # p is partitioning index, array[p]
        # is at right place
        k = new_partition(List, low, high)

        # Sort elements before partition
        # and after partition
        quick_sort(low, k - 1, List)
        quick_sort(k + 1, high, List)


# Driver code
array = [123, 10, 5, 2, 55, 664356, 44, 333, 2, -12, -12, 2, 2, 5, 7, 8, -12, 10,-12 ]
print(f'Starting array: {array}')
new_quick_sort(0, len(array) - 1, array)
print(f'Sorted array: {array}')
