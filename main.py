def bin_search(sorted_arr, sought_for):
    segment_start = 0
    segment_end = len(sorted_arr)

    while segment_start != segment_end:
        pivot = (segment_start + segment_end) // 2

        if sorted_arr[pivot] == sought_for:
            return pivot
        elif sorted_arr[pivot] > sought_for:
            segment_end = pivot - 1
        else:
            segment_start = pivot + 1

    return -1


if __name__ == '__main__':
    data_lst = [-4, -2, 5, 6, 7, 9, 10, 12, 13, 17, 18, 20, 24, 29, 30]
    num = 11
    res = bin_search(data_lst, num)
    if res != -1:
        print("Index {} is {}".format(num, res))
    else:
        print("Number {} was not found".format(num))
