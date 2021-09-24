from heapq import merge


def merge_multiple_seq(lists: list, k: int):
    """Merges k lists together sequentially."""
    if k == 2:
        return list(merge(lists[0], lists[1]))
    else:
        L = list(merge(lists[0], lists[1]))
        lists.remove(lists[0])
        lists.remove(lists[0])
        lists.append(L)
        return merge_multiple_seq(lists, len(lists))


def merge_multiple_div(lists: list, k: int):
    """Merges k lists together using divide & conquer.
    :note: This assumes k is a power of 2"""
    if k == 2:
        return list(merge(lists[0], lists[1]))
    else:
        l1 = merge_multiple_div(lists[:int(len(lists) / 2)], int(len(lists) / 2))
        l2 = merge_multiple_div(lists[int(len(lists) / 2):], int(len(lists) / 2))
        return list(merge(l1, l2))


def main():
    lists = [[1, 2, 5, 6], [8, 12, 14], [3, 7, 9, 222], [12323, 53464246, 56666666666], [-7, -5, -3, 1.5, 27, 4029],
             [-11, -10, -9], [100, 200, 300], [6000, 7000, 8000]]
    print(list(merge_multiple_div(lists, len(lists))))


if __name__ == '__main__':
    main()
