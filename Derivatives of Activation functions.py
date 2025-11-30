def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	import math as m
	def s(x):
		return 1/(1+m.exp(-x))
	def sd(x):
		return s(x)*(1-s(x))
	def td(x):
		return 1-(m.tanh(x))**2
	def rd(x):
		return 1 if x>0 else 0
	d = {}
	d['sigmoid'] = float(sd(x))
	d['tanh'] = float(td(x))
	d['relu'] = float(rd(x))
	return d

	pass
