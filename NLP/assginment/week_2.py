import numpy as np

a_np = np.array([[1, 2, 3], [4, 5, 6]])
b_np = np.array([[1, 3, 5], [2, 4, 6]])

r1 = np.any(a_np > 3)
r2 = np.all((a_np > 3))
r3 = a_np >= b_np
r4 = a_np[a_np >= b_np]
r5 = np.where(a_np > 2)
r6 = np.where(a_np > 2, a_np, 0)
r7 = np.where(a_np > 2, a_np * 2, 1)
r8 = np.argmax(a_np)
r9 = np.argmax(a_np, axis=1)
r10 = np.argmax(a_np, axis=0)
