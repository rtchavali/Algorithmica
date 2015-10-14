__author__ = 'KH1962'
import sets
def array_compare_common_elements(array1,array2):
    #sorted(array1)
    #sorted(array2)
    for x in range(len(array1)):
        for y in range(len(array2)):
            if array1[x]==array2[y]:
                print array1[x]
                break
            else:
                continue
array_compare_common_elements([1,2,3,4,3,2],[2,3,4,3,2])

def array_compare_common_elements_hashset(array1,array2):
    a=set(array1)
    b=set(array2)
    print a & b
array_compare_common_elements_hashset([1,2,3,4,3,2],[2,3,4,3,2])