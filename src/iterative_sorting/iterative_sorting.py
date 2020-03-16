# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)-1):
        current_item = arr[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        unsorted = arr[i+1:]
        unsorted_min = unsorted[0]
        for idx, item in enumerate(unsorted):
            if item < unsorted_min:
                unsorted_min = item
                unsorted_min_idx = i + idx + 1
        if unsorted_min < current_item:
            arr[i] = unsorted_min
            arr[unsorted_min_idx] = current_item
    return arr


# # TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    if len(arr)>0:
        condition_list = [False for i in arr]
        condition_list[-1] = True
        while False in condition_list:
            # loop through each index in the array
            for i in range(len(arr)-1):
                # if the item on the right is greater
                if arr[i+1] >= arr[i]:
                    # set sorted = True
                    condition_list[i] = True
                # if the item on the right is less, 
                else:
                    # swap the current item and the one to the right
                    current = arr[i]
                    right = arr[i+1]
                    arr[i+1] = current
                    arr[i] = right 
                    # if you swapped set sorted = false
                    condition_list[i] = False
                # print(arr)
    return arr

# arr = [0,0,2,40,1,5,0,0,5,3,5,4,8,9]
# print(bubble_sort(arr))


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr