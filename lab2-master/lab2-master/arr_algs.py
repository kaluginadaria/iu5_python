

def find_min (array):
    min = array[0]
    for a in array:
        if a < min :
            min = a
    return min

def sr_arifm (array):
    sum=0
    for a in array:
        sum+=a
    return sum/len(array)

array = [13,4,5,6,0.5]
print(find_min(array))
print (sr_arifm(array))