def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    import numpy as np
    a =np.array(matrix)
    a = scalar*a
	return a
