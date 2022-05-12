def sort_list(list1):
    copy_list = list1.copy()
    for j in range(1, len(copy_list)):
        for i in range(0, len(copy_list)):
            if copy_list[i] >= copy_list[j]:
                item = copy_list[j]
                copy_list[j] = copy_list[i]
                copy_list[i] = item
    return copy_list

input_list = [5, 12, 72, 8, 23, 45, 82, 136]
print(sort_list(input_list))
