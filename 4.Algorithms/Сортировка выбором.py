def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def find_high(arr):
    highest = arr[0]
    highest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            highest_index = i
    return highest_index


def selectionSort(arr, reverse=False):
    newArr = []
    if reverse == False:
        for i in range(len(arr)):
            smallest = find_Smallest(arr)
            newArr.append(arr.pop(smallest))
        return newArr
    else:
        for i in range(len(arr)):
            smallest = find_high(arr)
            newArr.append(arr.pop(smallest))
        return newArr


if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10], True))
