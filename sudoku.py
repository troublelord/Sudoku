def issafe(list,l,num):
    #if violates row
    for i in range(9):
        if list[l[0]][i] == num:
            return 0
    #if violates column
    for i in range(9):
        if list[i][l[1]] == num:
            return 0
    row=0
    col=0
    if l[0]<3:
        row=0
    elif l[0]<6:
        row=3
    else:
        row=6

    if l[1]<3:
        col=0
    elif l[1]<6:
        col=3
    else:
        col=6
    #if violates box
    for i in range(3):
        for j in range(3):
            if list[i+row][j+col] == num:
                return 0
                    
    return 1

#to find empty cells (with value 0)
def find_empty_loc(list,l):
    for i in range(9):
        for j in range(9):
            if list[i][j]==0:
                l[0]=i
                l[1]=j
                return 1
    #no more empty cells left
    return 0
    
def solve(list):
    
    l=[0,0]
    
    if(not find_empty_loc(list,l)):
        return 1
    
    row=l[0]
    col=l[1]

    for i in range(1,10):
        
        if(issafe(list,l,i)):
            list[row][col]=i
            if(solve(list)):
               return 1 #if solved
            else:
                list[row][col]=0
    #if not solved
    return 0 
        
   
    
    
    
    

'''
list=[[0 for i in range(1,10)  ] for i in range(1,10)]
#uncomment to input via console
for i in range(1,10):
        for i in range(1,10):
            list[i][j]=input();

'''
list=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]

if(solve(list)):
    for i in range(0,9):
        print(list[i])
else:
    print("No solution exists")

