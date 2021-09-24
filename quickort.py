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


def new_quick_sort(low, high, List):
    """A slightly modified version of quicksort that omits duplicate pivot elements from future recursive calls."""
    if low < high:
        # obtain the position of the last pivot element & the end of the '< pivot' list
        k, first_list_end = new_partition(List, low, high)

        # sort elements '< pivot'
        new_quick_sort(low, first_list_end, List)

        # sort elements '> pivot'
        new_quick_sort(k + 1, high, List)


def handle_duplicates(i, L: list, low, e):
    swap_index = i
    # iterate through the '<= pivot' portion of the list
    for k in range(low, i + 1):
        if swap_index <= k:
            break
        if L[k] == e:
            if L[swap_index] == e:
                swap_index = swap_index - 1
            exchange(L, swap_index, k)
            swap_index = swap_index - 1
    return swap_index


def quick_sort(low, high, List):
    """Traditional quicksort implementation"""
    if low < high:
        # p is partitioning index, array[p]
        # is at right place
        k = new_partition(List, low, high)

        # Sort elements before partition
        # and after partition
        quick_sort(low, k - 1, List)
        quick_sort(k + 1, high, List)


def main():
    # Driver code
    array = [4, 8, 3, 4, 4, 3, 2, 8, 2, 4, 3, 9, 8, 8, 4, 9, 4, 4, 2, 9]
    print(f'Starting array: {array}')
    new_quick_sort(0, len(array) - 1, array)
    print(f'Sorted array: {array}')


if __name__ == '__main__':
    main()
