from unittest import TestCase

from src.Point3D import Point3D


class TestPoint3D(TestCase):
    x1 = 35.18869800968523
    x2 = 35.187594216303474
    x3 = 35.19381366747377
    y1 = 32.104927164705884
    y2 = 32.10378225882353
    y3 = 32.102419275630254
    z = 0.0
    point1 = Point3D(x=x1, y=y1, z=z)
    point2 = Point3D(x=x2,  y=y2, z=z)
    point3 = Point3D(x=x3, y=y3, z=z)

    def test_get_x(self):
        self.assertEqual(self.point1.get_x(), self.x1)
        self.assertEqual(self.point2.get_x(), self.x2)
        self.assertEqual(self.point3.get_x(), self.x3)

    def test_get_y(self):
        self.assertEqual(self.point1.get_y(), self.y1)
        self.assertEqual(self.point2.get_y(), self.y2)
        self.assertEqual(self.point3.get_y(), self.y3)

    def test_get_z(self):
        self.assertEqual(self.point1.get_z(), self.z)
        self.assertEqual(self.point2.get_z(), self.z)
        self.assertEqual(self.point3.get_z(), self.z)

    def test_distance(self):
        dist1 = 0.0015903362251637298
        dist2 = 0.005697320618069602
        dist3 = 0.006367047671004182
        dist4 = 0.0
        self.assertEqual(dist1, self.point1.distance(self.point2))
        self.assertEqual(dist3, self.point2.distance(self.point3))
        self.assertEqual(dist4, self.point3.distance(self.point3))
        self.assertEqual(dist2, self.point3.distance(self.point1))

