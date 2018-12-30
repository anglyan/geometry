import unittest
import unitcell as uc

class TestVector(unittest.TestCase):

    def setUp(self):
        self.v1 = uc.geometry.Vector(1, 2, 3)
        self.v2 = uc.geometry.Vector(2, 2., 2)
        self.v3 = uc.geometry.Vector(2, -1, 0)

    def test_sum(self):
        vs = self.v1 + self.v2
        self.assertAlmostEqual(vs, uc.geometry.Vector(3, 4, 5))

    def test_sub(self):
        vs = self.v1 - self.v2
        self.assertAlmostEqual(vs, uc.geometry.Vector(-1, 0, 1))

    def test_copy(self):
        vs = self.v1.copy()
        self.assertIsNot(vs, self.v1)

    def test_inplace(self):
        vs = self.v1.translate(self.v1)
        self.assertIs(vs, self.v1)

if __name__ == '__main__':
    unittest.main()
