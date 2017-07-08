def intersec(x1, y1, x2, y2, x3, y3, x4, y4):

    return ((x1 <= x3 <= x2) or (x1 <= x4 <= x2)) or (x3 <= x1 <= x4) or (x3 <= x2 <= x4) and ((y1 >= y3 >= y2) or (y1 >= y4 >= y2) or (y3 >= y1 >= y4) or (y3 >= y2 >= y4))

def tarifa(m):

    if m <= 5: return 5

    elif 5 < m <= 10: return 7

    else: return 7 + (m - 10)

def pano_amarelo(x1, y1, x2, y2):

    from math import sqrt, pi

    d = y1 - y2

    r = d/2

    area_q = (d ** 2)/2

    area_c = pi * r ** 2

    return area_q - area_c