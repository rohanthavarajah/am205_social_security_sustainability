import numpy as np
from matplotlib import pyplot as plt

b = 0.01270
mu = 0.00799
beta = 1/22.0
gamma = 1/43.0
x0 = 1000000
y0 = 1000000
z0 = 1000000

def C(t):
	return (b + np.exp(-1*beta*t)*(-1*b + beta*x0)) / beta

def W(t):
	return ( (b*np.exp(gamma*t)/gamma) + 
		((-1*b + beta*x0)*np.exp(gamma*t - beta*t)/(gamma - beta)) -
		((b*beta - gamma*beta*x0 + y0*gamma**2 - y0*gamma*beta)/(gamma*(-1*gamma + beta))) ) * np.exp(-1*gamma*t)

def R(t):
	t1 = (-1*b*t + (np.exp(-1*beta*t)*(-1*b + beta*x0))/beta ) * (gamma/(-1*gamma + beta))
	t2 =  -1 * (np.exp(-1*gamma*t)*(b*beta - gamma*beta*x0 + y0*gamma**2 - y0*gamma*beta) / (gamma*(-1*gamma + beta))) * (gamma/(-1*gamma + beta))
	t3 = (b*t + (b*beta  - gamma*beta*x0 - y0*gamma*beta - z0*gamma*beta + gamma*b)/(gamma*beta)) * (gamma/(-1*gamma + beta))
	t4 = (np.exp(-1*gamma*t)*(b*beta - gamma*beta*x0 + y0*gamma**2 - y0*gamma*beta) / (gamma*(-1*gamma + beta)) + b*t) * (beta/(-1*gamma + beta))
	t5 = ((-b*beta + gamma*beta*x0 + y0*gamma*beta + z0*gamma*beta - gamma*b)/(gamma*beta) - b*t) * (beta/(-1*gamma + beta))
	return t1 + t2 + t3 + t4 + t5


times = np.linspace(0,100,100)
c = [C(t) for t in times]
w = [W(t) for t in times]
r = [R(t) for t in times]

plt.figure()
plt.plot(times,c, color="blue", label="children")
plt.plot(times,w, color="red", label="workers")
plt.plot(times,r, color="green", label="retirees")
plt.legend(loc="best")
plt.show()