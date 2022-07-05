#Importing numpy, scipy, mpmath and pyplo
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
#import subprocess
#import shlex
#end if

def tri_pdf(x):
    if x<0:
        return 0
    elif x<1:
        return x
    elif x<2:
        return (2-x)
    else:
        return 0
maxrange=50
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf=[]
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
#randvar = np.loadtxt('ln.dat',dtype='double')
randvar=np.loadtxt('tri.dat',dtype='double')
for i in range(0,maxrange):
    err_ind = np.nonzero(randvar < x[i]) #checking probability condition
    err_n = np.size(err_ind) #computing the probability
    err.append(err_n/simlen) #storing the probability values in a list

for i in range(0,maxrange-1):
    test = (err[i+1]-err[i])/(x[i+1]-x[i])
    pdf.append(test) #storing the pdf values in a list

vec_tri_pdf=scipy.vectorize(tri_pdf,otypes=[float])
plt.plot(x[0:(maxrange-1)],pdf,'o')
plt.plot(x,vec_tri_pdf(x))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical","Theory"])

#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window

