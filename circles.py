from math import pi 
def circle_area(r) : 
    return pi*pow(r, 2)

radii= [2, 0, -3, 2+5j, True, "radius"]
message= "area of the circle is {area} for a radiant of {radius} "

for r in radii: 
    A = circle_area(r)
    print( message.format(radius=r, area=A))