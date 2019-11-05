# Simplex Method to Solve Linear Programming Problem (Maximisation)
import numpy as np

CBi = np.array([0.0, 0.0])
Cj = np.array([12.0, 20.0, 0.0, 0.0])
Sol = np.array([100.0, 100.0])
Ratio = np.array([0.0, 0.0])
Zj = np.array([0.0, 0.0, 0.0, 0.0])
DiffCjZj = np.array([0.0, 0.0, 0.0, 0.0])
mat = np.array([
  [6.0, 8.0, 1.0, 0.0],
  [7.0, 12.0, 0.0, 1.0]
])
i = 0
j = 0
while i < len(Cj):
  val = 0
  while j < len(CBi):
    val += CBi[j] * mat[j, i]
    j += 1
  j = 0
  Zj[i] = val
  i += 1
i = 0
while i < len(Cj):
  DiffCjZj[i] = Cj[i] - Zj[i]
  i += 1
while len(DiffCjZj[DiffCjZj > 0]) != 0:
  keyColInd = np.argmax(DiffCjZj)
  j = 0
  while j < len(Ratio):
    Ratio[j] = Sol[j] / mat[j, keyColInd]
    j += 1
  keyRowInd = np.argmin(Ratio)
  keyElement = mat[keyRowInd, keyColInd]
  CBi[keyRowInd] = Cj[keyColInd]
  i = 0
  j = 0
  while i < len(CBi):
    if i == keyRowInd:
      mat[i, j] /= keyElement
      Sol[i] /= keyElement
      i += 1
    else:
      while j < len(Cj):
        mat[i, j] -= (mat[i, keyColInd] * mat[keyRowInd, j]) / keyElement
        j += 1
      j = 0
      Sol[i] -= (mat[i, keyColInd] * Sol[keyRowInd]) / keyElement
      i += 1
  i = 0
  j = 0
  while i < len(Cj):
    val = 0
    while j < len(CBi):
      val += CBi[j] * mat[j, i]
      j += 1
    Zj[i] = val
    j = 0
    i += 1
  i = 0
  # print (Zj)
  while i < len(Cj):
    DiffCjZj[i] = Cj[i] - Zj[i]
    i += 1
print ((CBi[0] * Sol[0]) + (CBi[1] * Sol[1]))
  
  


  
