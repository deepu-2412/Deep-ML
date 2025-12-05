def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
  import numpy as np
  a = np.array(matrix)
	return np.linalg.inv(a)
