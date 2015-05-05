import unittest
import math

import sys
sys.path.insert(0, '/home/jwright/Downloads/cadquery/')

from cadquery.pythonocc_impl.geom import Vector, Matrix
from OCC.gp import gp_Vec

class TestPythonOCC(unittest.TestCase):
    #TODO: Merge this with the one in tests/__init__.py
    def assertTupleAlmostEquals(self, expected, actual, places, msg):
        for i, j in zip(actual, expected):
            self.assertAlmostEquals(i, j, places, msg)

    def testVectorConstructors(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector((1, 2, 3))
        v3 = Vector(gp_Vec(1, 2, 3))
        v4 = Vector(Vector(1, 2, 3))

        for v in [v1, v2, v3, v4]:
            self.assertEqual((1, 2, 3), v.toTuple(), "A Vector object did not get constructed correctly: " + str(v))

    def testVectorLength(self):
        v1 = Vector(1, 2, 3)

        self.assertAlmostEquals(v1.Length, 3.74165738677, 3, "The length of a Vector object was calculated incorrectly: " + str(v1))

    def testVectorCross(self):
        v1 = Vector(3, -3, 1)
        v2 = Vector(4, 9, 2)

        v3 = v1.cross(v2)

        self.assertEqual((-15.0, -2.0, 39.0), v3.toTuple(), "The cross product of two Vector objects was calculated incorrectly: " + str(v1) + " - " + str(v2))

    def testVectorDot(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, -5, 6)

        dP = v1.dot(v2)

        self.assertEqual(dP, 12, "The dot product of two Vector objects was calculated incorrectly: " + str(v1) + " - " + str(v2))

    def testVectorSubtract(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)

        v3 = v1.sub(v2)

        self.assertEqual((-2, 0, 2), v3.toTuple(), "The subtraction of two Vector objects was calculated incorrectly: " + str(v1) + " - " + str(v2))

    def testVectorAdd(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)

        v3 = v1.add(v2)

        self.assertEqual((4, 4, 4), v3.toTuple(), "The addition of two Vector objects was calculated incorrectly: " + str(v1) + " - " + str(v2))

    def testVectorMultiply(self):
        v1 = Vector(1, 2, 3)
        scale = 2.0

        v2 = v1.multiply(scale)

        self.assertEqual((2, 4, 6), v2.toTuple(), "The multiplication of two Vector objects was calculated incorrectly: " + str(v1) + " - " + str(v2))

    def testVectorNormalize(self):
        v1 = Vector(1, 2, 3)

        vN = v1.normalize()

        self.assertTupleAlmostEquals((0.267, 0.535, 0.802), vN.toTuple(), 3, "A Vector object was normalized incorrectly: " + str(v1))

    def testVectorGetAngle(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)

        angle = v1.getAngle(v2)

        self.assertAlmostEquals(0.775, angle, 3, "The angle between two Vector objects was calculated incorrectly: " + str(v1) + " - " + str(v2))

    def testVectorInternals(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(3, 2, 1)
        v3 = Vector(1, 2, 3)
        v4 = Vector(4, 5, -6)

        v1.__hash__()
        v1.__add__(v2)
        v1.__repr__()
        v1.__str__()

        # Just test that the others don't raise exceptions, but make sure these give correct values
        len = v1.__len__()
        self.assertAlmostEquals(3.742, len, 3, "The length of a Vector object was calculated incorrectly: " + str(self))

        equal = v1.__eq__(v4)
        self.assertFalse(equal, "Two Vector objects that should not have been equal show equality: " + str(v1) + " - " + str(v4))
        equal = v1.__eq__(v3)
        self.assertTrue(equal)

    def testMatrixRotation(self):
        m1 = Matrix()

        m2 = m1.rotateX(math.pi)
        m3 = m1.rotateY(math.pi)

        print str(m2) + str(m3)

if __name__ == '__main__':
    unittest.main()