import math
#длина площадь

def lTr(x, InT):
    if InT == 'm': return x
    if InT == 'cm': return x/(100)
    if InT == 'mm': return x/(1000)
    if InT == 'km': return x*1000

def lenTrans(x, InT, ExT):
    if ExT == InT: return x
    a = lTr(x, InT)
    if ExT == 'mm': return a*(1000)
    if ExT == 'cm': return a*(100)
    if ExT == 'm': return a
    if ExT == 'km': return a/(1000)



def plTr(x, InT):
    if InT == 'm^2': return x
    if InT == 'cm^2': return x / (100**2)
    if InT == 'mm^2': return x / (1000**2)
    if InT == 'km^2': return x * (1000**2)

def plTrans(x, InT, ExT):
    if ExT == InT: return x
    a = plTr(x, InT)
    if ExT == 'mm^2': return a*(1000**2)
    if ExT == 'cm^2': return a*(100**2)
    if ExT == 'm^2': return a
    if ExT == 'km^2': return a/(1000**2)

