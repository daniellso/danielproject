def bubble_sort(data):

    list_len = len(data)-1

    for idx in range(list_len):
        for x in range(list_len-idx):
            if data[x] > data[x+1]:
                data[x], data[x+1] = data[x+1], data[x]


if __name__ == '__main__':
    data = [9, 8, 3, 6, 7]

    print(data)  # [9, 8, 3, 6, 7]

    bubble_sort(data)

    print(data)  # [3, 6, 7, 8, 9]   