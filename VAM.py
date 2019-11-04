import numpy as np
cost_mat = np.array([
  [19, 30, 50, 10],
  [70, 30, 40, 60],
  [40, 8, 70, 20],
])
supplies = [7, 9, 18]
demands = [5, 8, 7, 14]
cost = 0
# Ans 779
# Loop Until Either Row Penalty or Col Penalty is not possible
while cost_mat.size != 2:
  row_penalties = {}
  col_penalties = {}
  num = 0
  # Find Row Penalties
  for i in cost_mat:
      sortedRow = sorted(i)
      row_penalties[num] = sortedRow[1] - sortedRow[0]
      num += 1
  num = 0
  # Find Col Penalties
  for i in cost_mat.T:
      sortedCol = sorted(i)
      col_penalties[num] = sortedCol[1] - sortedCol[0]
      num += 1
  # Find the highest Penalty among row and col penalties
  if max(row_penalties.items(), key = lambda x: x[1])[1] > max(col_penalties.items(), key = lambda x: x[1])[1]:
      # If highest Penalty is among the row penalties, get its row num
      high = max(row_penalties.items(), key = lambda x: x[1])[0]
      # Get col index of Min cost from the row
      ind =  np.argmin(cost_mat[high, :])
      # Do necessary cost calculation and then delete entire row/col whichever becomes 0
      if demands[ind] < supplies[high]:
        cost += cost_mat[high, ind] * demands[ind]
        supplies[high] -= demands[ind]
        cost_mat = np.delete(cost_mat, ind, axis=1)
        del demands[ind]
      else:
        cost += cost_mat[high, ind] * supplies[high]
        demands[ind] -= supplies[high]
        cost_mat = np.delete(cost_mat, high, axis=0)
        del supplies[high] 
  else:
      high = max(col_penalties.items(), key = lambda x: x[1])[0]
      ind = np.argmin(cost_mat[:, high])
      if demands[high] < supplies[ind]:
        cost += cost_mat[ind, high] * demands[high]
        supplies[ind] -= demands[high]
        cost_mat = np.delete(cost_mat, high, axis=1)
        del demands[high] 
      else:
        cost += cost_mat[ind, high] * supplies[ind]
        demands[high] -= supplies[ind]
        cost_mat = np.delete(cost_mat, ind, axis=0)
        del supplies[ind] 
# Do this after no penalties is possible
rows = np.ma.size(cost_mat, 0)
cols = np.ma.size(cost_mat, 1)
ind = np.argmin(cost_mat)
row, col = np.unravel_index(ind, (rows, cols))
if demands[col] < supplies[row]:
  cost += cost_mat[row, col] * demands[col]
  supplies[row] -= demands[col]
  cost_mat = np.delete(cost_mat, col, axis=1)
  del demands[col]
else:
  cost += cost_mat[row, col] * supplies[row]
  demands[col] -= supplies[row]
  cost_mat = np.delete(cost_mat, row, axis=0)
  del supplies[row]
cost += cost_mat[0, 0] * demands[0]
print (cost)