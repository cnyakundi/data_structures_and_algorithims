from array import *

arr1= array('i', [1,2,3,4,5,6])

def searchArray(array,value):
    for i in array:
        if i ==value:
            return array.index(value)

    return "The element doesnt exist in the array"


print(searchArray(arr1,1))