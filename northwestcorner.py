def checkArray(arr):
    for i in arr:
        if (i != 0):
            return True
    return False

def getIndex(cost_mat, n, m):
    ind_i = 0
    ind_j = 0
    flag = 0
    for i in range(0, n):
    	for j in range(0, m):
    	    if (cost_mat[i][j] != 0):
    	        ind_i = i
    	        ind_j = j
    	        flag = 1
    	        break
    	if(flag == 1):
    	    break

    return ind_i, ind_j

cost_mat = [[19, 30, 50, 10],
     [70, 30, 40, 60],
     [40, 8, 70, 20]]
supply = [7, 9, 18]
demand = [5, 8, 7, 14]
n = 3
m = 4
index_i = 0
index_j = 0
cost = 0
while checkArray(supply) and checkArray(demand):
    index_i, index_j = getIndex(cost_mat, n, m)
    if supply[index_i] < demand[index_j]:
        cost = cost + (cost_mat[index_i][index_j] * supply[index_i])
        demand[index_j] = demand[index_j] - supply[index_i]
        supply[index_i] = 0
        for j in range(0, m):
            cost_mat[index_i][j] = 0
    else:
        cost = cost + (cost_mat[index_i][index_j] * demand[index_j])
        supply[index_i] = supply[index_i] - demand[index_j]
        demand[index_j] = 0
        for i in range(0, n):
            cost_mat[i][index_j] = 0
print('Final Cost: ', cost)