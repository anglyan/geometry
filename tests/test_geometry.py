import unittest

import geom3d as geom

class TestVec3(unittest.TestCase):

    def setUp(self):
        self.v1 = geom.Vec3(1, 2, 3)
        self.v2 = geom.Vec3(2, 2., 2)
        self.v3 = geom.Vec3(2, -1, 0)

    def test_sum(self):
        vs = self.v1 + self.v2
        self.assertAlmostEqual(vs, geom.Vec3(3, 4, 5))

    def test_sub(self):
        vs = self.v1 - self.v2
        self.assertAlmostEqual(vs, geom.Vec3(-1, 0, 1))

    def test_copy(self):
        vs = self.v1.copy()
        self.assertIsNot(vs, self.v1)

    def test_inplace(self):
        vs = self.v1.translate(self.v1)
        self.assertIs(vs, self.v1)

    def test_scalar(self):
        sc = geom.scalar(self.v1, self.v2)
        self.assertAlmostEqual(sc, 12)

if __name__ == '__main__':

    unittest.main()
