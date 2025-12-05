import math as m
def binomial_probability(n, k, p):
	"""
    Calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
    each with probability p of success, using the Binomial distribution formula.
    """
	# Your code here
  a = m.factorial(n)/(m.factorial(n-k)*m.factorial(k))
  prob = a * p**k * (1-p)**(n-k)
	return round(prob, 5)
