import numpy as np
import matplotlib.pylab as py
a = np.linspace(0,2)
z1 = np.sin(a-2)**2
z2 = np.exp(-(a**2))
z = z1*z2
py.plot(a,z,'k--')
py.xlabel('Int')
py.ylabel('Function - f(z)')
py.title('Plot a funtion with \'matplotlib\'') 
py.show()