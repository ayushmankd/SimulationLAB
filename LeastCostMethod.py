import numpy as np
mat = np.array([
  [19, 30, 50, 10],
  [70, 30, 40, 60],
  [40, 8, 70, 20],
])
supplies = np.array([7, 9, 18])
demands = np.array([5, 8, 7, 14])
# Answer 814
cost = 0
# Loop until Matrix contains 0 elements
while (mat.size != 0):
  # Finding Num of Rows and Cols of the Matrix
  rows = len(mat)
  cols = len(mat[0])
  # Finding Index of Minimum as an array
  minIndex = np.argmin(mat)
  # Finding the Corresponding Row, Col of the Minm Index
  row, col = np.unravel_index(minIndex, (rows, cols))
  # Checking whether Supplies or demands is lower
  if (supplies[row] < demands[col]):
    # Supplies is Lower
    # Cost is added
    # Cost = Supplies * Cost/item
    cost += supplies[row] *  mat[row, col]
    demands[col] -= supplies[row]
    # Supplies is made zero
    # Therefore no more operations possible on the Column therefore deleting
    supplies = np.delete(supplies, row)
    mat = np.delete(mat, row, axis=0)
  else:
    # Demand is Lower
    # Cost is added
    # Cost = Demand * Cost/item
    cost += demands[col] * mat[row, col]
    supplies[row] -= demands[col]
    # Demand is made zero
    # Therefore no more operations possible on the Column therefore deleting
    demands = np.delete(demands, col)
    mat = np.delete(mat, col, axis=1)
print (cost)