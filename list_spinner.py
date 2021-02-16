list_awal = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

# print(angka[0][3])
# print(angka[1][3])
# print(angka[2][3])
# print(angka[3][3])

def counterClockwise(arr):
    new_lists = []
    for i in range((len(arr)-1), -1, -1):
        temporary_row = []
        for j in range(len(arr)):
            temporary_row.append(arr[j][i])
        new_lists.append(temporary_row)
    return new_lists


print(counterClockwise(list_awal))
