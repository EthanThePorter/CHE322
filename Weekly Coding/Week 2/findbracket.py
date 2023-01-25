#file to search for initial guesses that bracket the root of xlnx-x

import matplotlib.pyplot as plt
from numpy import log,linspace,zeros,sign

f = lambda x : x*log(x)-x

#please note that the function above is equivalent to 
def f(x):
	return x*log(x)-x
	
#but since its simple enough to be written in one line, 
#we can use lambda functions. 
#if you would like to read more on this, https://realpython.com/python-lambda/
want_plot = False 

if want_plot:
	x_plot= linspace(0.1,6)
	plt.figure()
	plt.plot(x_plot,f(x_plot))
	plt.plot(x_plot,zeros(x_plot.size),'r--')
	plt.xlabel('x')
	plt.ylabel('x ln(x)-x')
	plt.show()
	
	
xmin = 0.1
xmax = 6
n=10 # number of points 

x_check=linspace(xmin,xmax,n)

for i in range(n-1):
	fx_min=f(x_check[i])
	fx_max=f(x_check[i+1])
	
	if sign(fx_min)!=sign(fx_max):
		xmin=x_check[i]
		xmax=x_check[i+1]
		break

if xmax==6:
	print("no bracket found")
else:
	print(f"bracket found at xmin={xmin} and xmax={xmax}")	