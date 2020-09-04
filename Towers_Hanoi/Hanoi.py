# -*- coding: utf-8 -*-

n = input("input number of rings for Hanoi: \n")

array = []
def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
    global array
    if n == 1: 
        array.append([from_rod, to_rod]) 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    array.append([from_rod, to_rod]) 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
    

def visual(n): #n is how many things are getting moved
    a = list(range(1,n+1))
    b = []
    c = []
    
    print("\n\n")
    print(a,c,b, " start")
    print("#############")
    
    for i in array: #array in instructions
        e1 = i[0]
        e2 = i[1]
        
        if e1 == "a":
            from_s = a
        elif e1 == "b":
            from_s = b
        elif e1 == "c":
            from_s = c
        
        if e2 == "a":
            to_s = a
        if e2 == "b":
            to_s = b
        if e2 == "c":
            to_s = c
            
        transfer = from_s.pop()
        to_s.append(transfer)
        print(a,b,c)
    
    print("############")
    print(a,c,b, " end")
    

TowerOfHanoi(n, 'a', 'b', 'c')
visual(n)
