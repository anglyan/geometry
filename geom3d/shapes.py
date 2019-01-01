import geom3d as geom

from math import sqrt

class Sphere:

    def __init__(self, c, rad):

        self.center = c
        self.rad = rad

    def move(self, v):
        self.center += v


class Line:

    def __init__(self, p, u):

        self.p = p
        self.u = geom.unit(u)


def calc_raytosphere(sp, li):
    """Calculate the intersection between a ray and a sphere, returning
     the distance between the ray origin and the shere or
     -1.0 if the two do not intersect"""

    oc = li.p - sp.center
    loc = geom.scalar(li.u, oc)
    uu = geom.scalar(li.u, li.u)
    delta = loc**2 - geom.scalar(oc, oc) + sp.rad**2
    if delta <= 0:
        return -1.0
    else:
        a1 = (-loc + sqrt(delta))/uu
        a2 = (-loc - sqrt(delta))/uu
        if a1 < 0:
            if a2 < 0:
                return -1.0
            else:
                return a2
        elif a2 < 0:
            return a1
        else:
            return min(a1, a2)
