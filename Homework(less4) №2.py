list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([j for i, j in enumerate(list_1) if i != 0 and j > list_1[i-1]])

