from copy import deepcopy


def spiral(matrix,f_list):

    row = len(a)
    col = len(a[0])
    top = True
    right = False
    bottom = False
    left = False
    dup = matrix
    if not matrix:
        dup = deepcopy(a)
    final_list = f_list
    i = 0
    if top:
        for idx in dup[0]:
            if idx != 'True':
                final_list.append(idx)
            indx = dup[0].index(idx)
            dup[0][indx] = 'True'
        top = False
        left = True       
    if left:
        start = None
        if i == 0:
            start = 1
        else:
            start = 0
        for r in range(start, row): 
            value = dup[r][col-1]
            if value != 'True':             # r is dynamic , read row by row
                final_list.append(value) 
            dup[r][col-1] = 'True'    # -1 to get final idx
        i+=1
        left = False
        bottom = True
    if bottom:
        start = None
        if i == 0:
            start = 1
        else:
            start = 0
        j = col-1 # to itr from reverse count
        for c in range(start,col):
            value = dup[row-1][j-c]
            if value != 'True':
                final_list.append(value)
                dup[row-1][j-c] = 'True'
        
        bottom= False
        right = True
    if right:
        k = row-1
        for itr in range(row):
            value = dup[k-itr][0]
            if value != 'True':
                final_list.append(value)
                dup[k-itr][0] = 'True'

        top = True
        right = False
    count = 0
    dup_len = len(dup)
    dup_copy = dup.copy()
    for itr in range(len(dup_copy)):
        if dup_copy[itr].count("True") == len(dup_copy[itr]):
            count+=1
            dup.remove(dup_copy[itr])

    if  count == dup_len:
        return final_list
    else:
        spiral(dup,final_list)
        pass
    return final_list



a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

if __name__=="__main__":
  print(spiral(a, f_list=[]))
 
