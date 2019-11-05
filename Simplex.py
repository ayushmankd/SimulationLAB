# Simplex Method to Solve Linear Programming Problem
import numpy as np

def getDiff(Cj, Zj):
  arr = [Cj[i] - Zj[i] for i in range(len(Cj))]
  return arr
def calculateZj(CBi, mat):
  i = 0
  j = 0
  arr = [0 for i in mat[0]]
  while j < len(arr):
    while i < len(CBi):
      arr[j] += CBi[i] * mat[i, j]
      i += 1
    j += 1
  return arr
def updateRatios(mat, keyRowInd):
  arr = [0 for i in mat]
  for i in range(len(mat)):
    arr = mat[i, -1] / mat[i, keyRowInd]
  return arr
def updateMat(mat, keyElement, keyColInd, keyRowInd):
  i = 0
  j = 0
  while i < len(mat):
    if i == keyRowInd:
      while j < len(mat[0]):
        mat[i, j] /= keyElement
        j += 1
    else:
      while j < len(mat[0]):
        mat[i, j] -= (mat[i, keyColInd] * mat[keyRowInd, j]) / keyElement
        j += 1
    i += 1
Cj = np.array([12.0, 16.0, 0.0, 0.0])
Zj = np.array([0.0, 0.0, 0.0, 0.0])
ratios = np.array([0.0, 0.0])
mat = np.array([
  [10.0, 20.0, 1.0, 0.0, 120.0],
  [8.0, 8.0, 0.0, 1.0, 80.0]
])
CBi = np.array([0.0, 0.0])
diff = np.array([0.0, 0.0, 0.0, 0.0])
Zj = np.asarray(calculateZj(CBi, mat))
diff = np.asarray(getDiff(Cj, Zj))
while len(diff[diff > 0]) > 0:
  keyColInd = np.argmax(diff)
  ratios = np.asarray(updateRatios(mat, keyColInd))
  keyRowInd = np.argmin(ratios)
  keyElement = mat[keyRowInd, keyColInd]
  updateMat(mat, keyElement, keyColInd, keyRowInd)
  CBi[keyRowInd] = Cj[keyColInd]
  Zj = np.asarray(calculateZj(CBi, mat))
  diff = np.asarray(getDiff(Cj, Zj))
  print (mat)
  # break
print ("Solution: ", Zj[-1])


  
