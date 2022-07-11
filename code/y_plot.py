import matplotlib.pyplot as plt
import numpy as np
y=np.loadtxt("y.dat")
plt.grid()
plt.plot(y,"o")
plt.show()
