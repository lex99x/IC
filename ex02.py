from math import *

def tarifa(m):

    if m <= 5:
        return 5
    elif 5 < m <= 10:
        return 7
    else:
        return 7 + (m - 10)

def pano_amarelo(x1, y1, x2, y2):

    d = y1-y2

    r = d/sqrt(2)

    areaq = (d**2)//2

    areac = pi*r**2
    
    return areaq - areac