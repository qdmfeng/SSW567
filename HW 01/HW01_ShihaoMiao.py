import unittest
import math


def classify_triangle(a, b, c):
    """returns a string that specifies whether the triangle is scalene, isosceles, or equilateral,
    and whether it is a right triangle as well."""
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Not a valid triangle")
    s = ""
    l = sorted([a, b, c])
    if math.isclose(l[0] ** 2 + l[1] ** 2, l[2] ** 2, rel_tol=1e-2):
        s += "Right "
    if a == b == c:
        s += "Equilateral"
    elif a == b or b == c or c == a:
        s += "Isosceles"
    else:
        s += "Scalene"
    return s


def main():
    x, y, z = map(int, input("Enter a three value: ").split())
    print(classify_triangle(x, y, z))


class TestTriangles(unittest.TestCase):
    def test_classify_triangle(self):
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, 3)
        self.assertEqual("Right Scalene", classify_triangle(3, 4, 5))
        self.assertEqual("Equilateral", classify_triangle(6, 6, 6))
        self.assertEqual("Isosceles", classify_triangle(4, 4, 6))
        self.assertEqual("Scalene", classify_triangle(5, 6, 7))
        self.assertEqual("Right Isosceles", classify_triangle(1, 1, math.sqrt(2)))
        with self.assertRaises(ValueError):
            classify_triangle(0, 0, 0)
        with self.assertRaises(ValueError):
            classify_triangle(1, -2, 3)

if __name__ == '__main__':
    main()
