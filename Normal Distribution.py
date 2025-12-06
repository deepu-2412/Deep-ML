import math as m

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
    val = m.e**(-0.5*((x-mean)/std_dev)**2)/m.sqrt(2*m.pi*std_dev**2)
	pass

	return round(val,5)
