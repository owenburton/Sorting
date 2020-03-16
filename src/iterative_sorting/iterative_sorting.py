# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
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
# def bubble_sort( arr ):

#     return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr