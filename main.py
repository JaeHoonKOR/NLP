import numpy as np

a_np = np.array([[1, 2, 3], [4, 5, 6]])
b_np = np.array([[1, 3, 5], [2, 4, 6]])

# 배열 a_np에서 3보다 큰 요소가 하나라도 있는지 검사하여 결과 반환
r1 = np.any(a_np > 3)

# 배열 a_np의 모든 요소가 3보다 큰지 검사하여 결과 반환
r2 = np.all((a_np > 3))

# 배열 a_np와 b_np의 요소를 비교하여, a_np의 요소가 b_np의 요소 이상인 경우 True 반환
r3 = a_np >= b_np

# 배열 a_np에서 조건을 만족하는 요소만 추출하여 배열 생성
r4 = a_np[a_np >= b_np]

# 배열 a_np에서 2보다 큰 요소의 인덱스를 반환하는 배열 생성
r5 = np.where(a_np > 2)

# 배열 a_np에서 2보다 큰 요소는 그대로, 작거나 같은 요소는 0으로 대체하여 배열 생성
r6 = np.where(a_np > 2, a_np, 0)

# 배열 a_np에서 2보다 큰 요소는 그대로, 작거나 같은 요소는 1로 대체하여 배열 생성
r7 = np.where(a_np > 2, a_np * 2, 1)

# 배열 a_np에서 최댓값의 인덱스를 반환
r8 = np.argmax(a_np)

# 배열 a_np에서 각 행의 최댓값의 인덱스를 반환하는 배열 생성
r9 = np.argmax(a_np, axis=1)

# 배열 a_np에서 각 열의 최댓값의 인덱스를 반환하는 배열 생성
r10 = np.argmax(a_np, axis=0)

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print(r8)
print(r9)
print(r10)
#
