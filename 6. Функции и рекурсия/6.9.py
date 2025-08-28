import random as rn

def drop():
    return rn.randint(1, 6)

def two_drops(n):
    drop_list = []
    
    i = n
    while i > 0:
        drop_list.append(drop() + drop())
        i -= 1

    print(drop_list)
    counlist = [0] * 12

    while i < 13:
        
        count_val = 0
        j = n
        
        while j > 0:
            if droplist[j] == i:
                count_val += 1
            j -= 1
            
        countlist[i] = count_val
        
        i += 1
    

two_drops(int(input()))
    

    
