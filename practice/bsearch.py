def bsearch(x, xs, imin, imax):

	imeio = (imin + imax)//2

	if imin == imax: 
		
		return imin

	elif x > xs[imeio]: 
		
		return bsearch(x, xs, imeio + 1, imax)

	else: 
		
		return bsearch(x, xs, imin, imeio)

def onde(x, xs): 
	
	return bsearch(x, xs, 0, len(xs) - 1)