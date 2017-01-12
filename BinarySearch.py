lst = raw_input('Enter array: ')
target = raw_input('Enter target value:')

def BinarySearch(lst, target):
    tg = int(target)
    numlist = list()
    l = lst.split(',')
    
    for numb in l:
        n = int(numb)
        if n not in numlist:
            numlist.append(n)
    
    min = 0
    max = len(numlist)
    
    while max >= min:
        guess = (max + min) / 2
        
        if tg > len(numlist):
            print 'Number not in array'
            break
            
        elif numlist[guess] == tg:
            print 'Index of target:', guess
            break
        
        elif numlist[guess] < tg:
            min = guess + 1
        
        else:
            max = guess - 1
            
    if max < min:
        print 'Number not in array'
        
   
BinarySearch(lst, target)