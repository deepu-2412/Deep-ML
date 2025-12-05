def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import pandas as pd
	df = pd.DataFrame(matrix)
	if mode=='column':
		return df.mean(axis=0).tolist()
	if mode=='row':
		return df.mean(axis=1).tolist()
	
