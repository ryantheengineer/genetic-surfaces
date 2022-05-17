import numpy as np
import matplotlib.pyplot as plt
import random

def random_curve(npts,xrange,maxdepth,nsines,arange,brange,crange):
    """
    Generate a random curve with inputs ___________

    Returns X and Y vectors for plotting.
    """
    X = np.linspace(xrange[0],xrange[1],npts,endpoint=True)

    depth = maxdepth + 1
    maxiter = 5000
    iteration = 0

    while depth > maxdepth:
        Y = np.zeros(len(X))
        for i in range(nsines):
            a = random.uniform(arange[0],arange[1])
            b = random.uniform(brange[0],brange[1])
            c = random.uniform(crange[0],crange[1])
            Ytemp = a*np.sin(b*X + c)
            Y += Ytemp

        depth = np.max(Y) - np.min(Y)

        iteration += 1
        if iteration > maxiter:
            print("Reached max iterations: {}".format(maxiter))
            break

    return X, Y, iteration


if __name__ == '__main__':
    npts = 200
    xrange = (0,10)
    maxdepth = 2
    nsines = random.randint(100,300)
    arange = (-1, 1)
    brange = (0.1,10)
    crange = (-np.pi, np.pi)
    X,Y,iteration = random_curve(npts,xrange,maxdepth,nsines,arange,brange,crange)
    print(iteration)
    plt.plot(X,Y)
