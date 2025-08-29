import random as rn
import heapq

def drop():
    return rn.randint(1, 6)

def two_drops(n):
    drop_list = []
    
    i = n
    while i > 0:
        drop_list.append(drop() + drop())
        i -= 1

    countlist = dict()

    while i < 13:
        
        count_val = 0
        j = n - 1
        
        while j > 0:
            if drop_list[j] == i:
                count_val += 1
            j -= 1
            
        countlist[i] = count_val
        i += 1

    return heapq.nlargest(3, countlist.items(), key = lambda item: item[1])
    

print(two_drops(int(input())))
    

    
