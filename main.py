import math
import random

def GFT(data : list, start: int, class_interval : int = None , quantity_class : int = None):
    data.sort()
    print('processing...')
    if class_interval == None and quantity_class != None:
        Max = max(data) # Maximum
        Min = min(data) # Minimum
        Checked = (Max - Min) / quantity_class
        class_interval = math.ceil((Max - Min) / quantity_class) # range / quantity class
        if str(Checked).endswith(".0"):
            quantity_class += 1
        
    elif class_interval != None and quantity_class == None:
        Max = max(data) # Maximum
        Min = min(data) # Minimum
        Checked = (Max - Min) / class_interval
        quantity_class = math.ceil((Max - Min) / class_interval) # range / class interval
        if str(Checked).endswith(".0"):
            quantity_class += 1
    else:
        raise AttributeError("")

    nfe = start # N for exec
    
    for i in range(quantity_class):
        exec(f"nfu{nfe} = 0") # N for use
        nfe += class_interval # Create variables by using start += class interval 
    
    nfc = start # N for check
    
    for elements in data:
        while elements > nfc+class_interval-1: # if the data in sorted list > maximum value in that column
            nfc += class_interval
        else: # if data in sorted list < maximum value in that column
            exec(f"nfu{nfc} += 1") # count the sorted data in the range of that column
    
    n = start
    loop = quantity_class
    for i in range(loop): 
        # first is the class
        # second is the first number of range in that class
        # third is last number of range in that class
        # fourth is count of number in that class
        # fifth is lower of that class
        # sixth is upper of that class
        # seventh is number is in the center of that class
        exec(f"print('|',i+1,'|', '|',n,'-',n+class_interval-1,'|', ',',nfu{n},',',(n+(n-1))/2,',', ((n+class_interval-1)+n+class_interval)/2,',',(n+n+class_interval-1)/2)") # display
        n += class_interval # using it for display

# working
if __name__ == '__main__':
    
    # Example
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    GFT(data = data, start = min(data), class_interval=5, quantity_class=None)
