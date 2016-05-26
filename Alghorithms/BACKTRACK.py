def check_constraints(mat):
    for i in range(9):
        row = mat[i][0:9];
        numbers = [];
        for element in row:
            if (element != 0):
                if (element in numbers):
                    return False;
                else:
                    numbers.append(element);

    for j in range(9):
        col = mat[0:9][j];
        numbers = [];
        for element in col:
            if (element != 0):
                if (element in numbers):
                    return False;
                else:
                    numbers.append(element);

    INDEXES  = [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)];
    for index in INDEX:
        row = index[0];
        col = index[1];
        numbers = [];
        for i in range(3):
            for j in range(3):
                element = mat[row+i][col+j];
                if (element != 0):
                    if (element in numbers):
                        return False;
                    else:
                        numbers.append(element);
    return True;


def iscomplete(mat):
    for i in range(9):
        for j in range(9):
            if(mat[i][j] == 0):
                return False;
    return True;


def check_row(mat,pos,val):
    row = pos[0];
    for i in range(9):
        if (mat[row][i] == val):
            return False;
    return True;


def check_col(mat,pos,val):
    col = pos[1];
    for j in range(9):
        if (mat[j][col] == val):
            return False;
    return True;


def check_square(mat,pos,val):
    row = pos[0]/3;
    col = pos[1]/3;
    for i in range(3):
        for j in range(3):
            if (mat[3*row+i][3*col+j] == val):
                return False;
    return True;


def check_pos(mat,pos,val):
    row = check_row(mat,pos,val);
    col = check_col(mat,pos,val);
    sqr = check_square(mat,pos,val);
    
    res = row and col and sqr;
    return res;


def no_val(mat):
    for r in range(9):
        for c in range(9):
            if (mat[r][c] == 0):
                return (r,c);


def copy(A):
    B = [];
    for i in range(len(A)):
        B.append([]);
    for i in range(len(A)):
        B[i] = A[i][:];
    return B;


def backtrack(mat,depth):
    if iscomplete(mat):
        return (mat,True);
    pos = no_val(mat);
    for val in range(1,10):
        if (check_pos(mat,pos,val)):
            newmat = copy(mat);
            newmat[pos[0]][pos[1]] = val;
            result = backtrack(newmat,depth+1);
            if (result != False):
                return result;
    return False