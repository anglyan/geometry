import unittest

import geom3d as geom
import geom3d.shapes as sh

class TestShapes(unittest.TestCase):

    def setUp(self):
        self.center = geom.Vec3(2, 2, 3)
        self.pl = geom.Vec3(0, 0, 0)
        self.vec = geom.Vec3(2, 2, 3.5)

    def test_createSphere(self):
        sp1 = sh.Sphere(self.center, 1.0)
        self.assertAlmostEqual(sp1.rad, 1.0)

    def test_createLine(self):
        ln = sh.Line(self.pl, self.vec)
        self.assertAlmostEqual(abs(ln.u), 1.0)

    def test_raytosphere(self):
        ln = sh.Line(self.pl, self.vec)
        sp = sh.Sphere(self.center, 1.0)
        self.assertTrue(sh.calc_raytosphere(sp,ln) > 0 )
        ln2 = sh.Line(self.pl, geom.Vec3(1,0,0))
        sp2 = sh.Sphere(geom.Vec3(2,0,0),1.5)
        self.assertAlmostEqual(sh.calc_raytosphere(sp2, ln2), 0.5)
        ln3 = sh.Line(self.pl, geom.Vec3(-1,0,0))
        sp3 = sh.Sphere(geom.Vec3(-2,0,0),1.5)
        self.assertAlmostEqual(sh.calc_raytosphere(sp3, ln3), 0.5)
        ln4 = sh.Line(self.pl, geom.Vec3(1,0,0))
        sp4 = sh.Sphere(geom.Vec3(-2,0,0),1.5)
        self.assertTrue(sh.calc_raytosphere(sp4, ln4) < 0)


if __name__ == '__main__':

    unittest.main()
