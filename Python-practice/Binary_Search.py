def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)
        
data = [2,4,5,6,7,8,9,10,21,35,64,76,99,101,120,121,140,155,164,189,290,291]

print(binary_search(data, 121, 0, len(data)))