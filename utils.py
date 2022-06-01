def bubblesort(list):
    # Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        nxt_element = InputList[i]
        j = i-1
        # Compare the current element with next one
        while (InputList[j] > nxt_element and j >= 0):
            InputList[j+1] = InputList[j]
            j -= 1
        InputList[j+1] = nxt_element
    return  InputList


def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx+1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        # Swap the minimum value with the compared value
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
    return input_list

def insertion_sort_yeild(InputList):
    for i in range(1, len(InputList)):
        nxt_element = InputList[i]
        j = i-1
        # Compare the current element with next one
        while (InputList[j] > nxt_element and j >= 0):
            InputList[j+1] = InputList[j]
            j -= 1
            yield InputList
        InputList[j+1] = nxt_element
        yield  InputList


def selection_sort_yeild(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx+1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
                yield input_list
        # Swap the minimum value with the compared value
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
        yield input_list