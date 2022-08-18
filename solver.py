board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



def find_solution(ls):
    next_box = find_empty(ls)
    if next_box == None:
        return True
    else:
        for i in range(0,10):
            if is_valid(ls,i,next_box[0],next_box[1]):
                ls[next_box[0]][next_box[1]] =i
                
                if find_solution(ls):
                    return True
                    
                ls[next_box[0]][next_box[1]] =0
        return False  
            
def find_empty(ls):
    for r in range(0,9):
       for c in range(0,9):
            if ls[r][c] == 0:
                return r,c
    return None

def is_valid(ls,num,r,c):
    #for the rows
    for i in ls[r]:
        if i == num:
            return False
    #for the columns 
    for i in range(0,9):
        if ls[i][c] == num:
            return False
    #for the box
    rows  = (r // 3)*3
    columns = (c // 3)*3 
    for i in range(rows,rows+3):
        for k in range(columns,columns+3):
            if(ls[i][k] == num):
                return False
    return True

find_solution(board)
for i in board:
    print(i)