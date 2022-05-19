import numpy as np
from aaaFunction import constants as c
def lorentzian(x,x0,fwhm):
    gamma =  fwhm/2
    x0 = np.ones(len(x))*x0
    f = (1/(c.pi)*gamma)*(gamma**2/((x-x0)**2+gamma**2))
    return(f)

