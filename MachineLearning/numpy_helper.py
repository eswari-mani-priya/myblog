## __author__ == "Priya"

import numpy as np


def array_from_list(listdata):
    array = np.array(listdata)
    return array


def float_array_from_list(listdata):
    array_float = np.array(listdata, dtype='float')
    return array_float


def convert_arr_to_int(arr):
    arr_int = arr.astype('int')
    return arr_int


def convert_arr_to_str(arr):
    arr_str = arr.astype('str')
    return arr_str


def bool_array(listdata):
    arr_bool = np.array(listdata, dtype='bool')
    return arr_bool


#Create object array to hold numbers as well as strings
def object_array(listdata):
    arr_obj = np.array(listdata, dtype='object')
    return arr_obj


def list_from_array(arr):
    listdata = arr.tolist()
    return listdata


def get_array_attributes(arr):
    attr = {}
    attr['shape'] = arr.shape
    attr['dtype'] = arr.dtype
    attr['size'] = arr.size
    attr['ndim'] = arr.ndim
    return attr


def reverse_arr_rows(arr):
    arr_rev = arr[::-1, ]
    return arr_rev


def reverse_arr(arr):
    arr_rev = arr[::-1, ::-1]
    return arr_rev


def get_mean_min_max(arr):
    val={}
    val['mean'] = arr.mean()
    val['min'] = arr.min()
    val['max'] = arr.max()
    return val


def get_row_col_wise_min(arr):
    row_min = np.amin(arr, axis=1)
    col_min = np.amin(arr, axis=0)
    return row_min, col_min


def get_cummulative_sum(arr):
    cumsum = np.cumsum(arr)
    return cumsum


if __name__ =="__main__":
    listdata = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]
    arr1 = array_from_list(listdata)
    print("List1: ", listdata)
    print("Array From List: ", arr1)
    arr2 = float_array_from_list(listdata)
    print("Float Array from List: ", arr2)
    int_arr = convert_arr_to_int(arr2)
    print("Convert Array to Float: ", int_arr)
    str_arr = convert_arr_to_str(int_arr)
    print("Convert Array to String: ", str_arr)
    list2 = [1,0,3,4,0,10]
    bool_arr = bool_array(list2)
    print("List2: ", list2)
    print("Boolean Array: ", bool_arr)
    list3 = [1, "Hello", 59.6]
    obj_arr = object_array(list3)
    print("List3: ", list3)
    print("Object Array: ", obj_arr)
    list_from_arr = list_from_array(arr1)
    print("List1 from Array: ", list_from_arr)
    attr = get_array_attributes(arr1)
    print("Attributes : ", attr)
    rev_arr_row = reverse_arr_rows(arr1)
    print("Reverse Array Rows: ", rev_arr_row)
    rev_arr = reverse_arr(arr1)
    print("Reverse Array: ", rev_arr)
    mean_min_max_vals = get_mean_min_max(arr1)
    print("Mean_MIN_Max_Values: ", mean_min_max_vals)
    row_col_min = get_row_col_wise_min(arr1)
    print("Row_Col_Wise_min: ", row_col_min)
    cumsum = get_cummulative_sum(arr1)
    print("Cummualative Sum of Array: ", cumsum)





