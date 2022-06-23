def list_max(input_list):
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    print(max_value)
    return(max_value)


list1 = [1, 2, 12, -3, 5, -7, 8]
print(list_max(list1))

list2 = [34, 56, -24, -45, 98, -23]
list_max(list2)
