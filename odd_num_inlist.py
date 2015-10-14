__author__ = 'KH1962'
#import itertools
def nonrepeated_xor(array):
    res=0
    for x in range(len(array)):
        res=res^array[x]
    return res
print nonrepeated_xor([1,2,3,3,2,1,4,4,5])

#Navie method

def nonrepeated_compare(array):
    #sorted(array)
    for x in range(len(array)):
        dup=False
        for y in range(len(array)):
            if x == y:
                continue
            if array[x]==array[y]:
                dup=True
                break
        if dup==False:
            print array[x]
print nonrepeated_compare([2,3,4,4,3,2,1,6])
print nonrepeated_compare([1,2,3,3,6,7,7])



        
