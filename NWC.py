import numpy as np
cost_mat = np.array([
  [5, 8, 4],
  [6, 6, 3],
  [3, 9, 6]
])
supplies = np.array([50, 40, 60])
demands = np.array([20, 95, 35])
i = 0
col_num = 0
row_num = 0
cost = 0
num_elements = len(supplies) + len(demands) - 1
while (i < num_elements):
  if (row_num == len(supplies)) or (col_num == len(demands)):
    break
  if supplies[row_num] < demands[col_num]:
    cost += supplies[row_num] * cost_mat[row_num, col_num]
    demands[col_num] -= supplies[row_num]
    supplies[row_num] = 0
    row_num += 1
    pass
  else:
    cost += demands[col_num] * cost_mat[row_num, col_num]
    supplies[row_num] -= demands[col_num]
    demands[col_num] = 0
    col_num += 1
    pass
  i += 1
print (cost)
