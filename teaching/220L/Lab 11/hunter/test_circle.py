import circle, point
from tester import test


def main():
    test('Circle exists', lambda: circle.Circle)
    test('Circle imports point.Point', lambda: 'point' in circle.__dict__ or circle.Point.__module__ == 'point', True)
    c = test('Constructor accepts (5, 10, 3.5)', lambda: circle.Circle(5, 10, 3.5))
    c2 = test('Constructor accepts (1, 1, -5)', lambda: circle.Circle(1, 1, -5))
    test('Constructor with (radius < 0) sets radius to 0', lambda: c2.get_radius(), 0)
    test('Method get_center() returns Point', lambda: type(c.get_center()), point.Point)
    test('Method get_center() returns (5,10)', lambda: (c.get_center().get_x(), c.get_center().get_y()), (5, 10))
    test('Method get_radius() returns 3.5', lambda: c.get_radius(), 3.5)
    test('Method set_center() is void', lambda: type(c.set_center(1, 2)), type(None))
    test('Method set_center(1, 2) updates center', lambda: (c.get_center().get_x(), c.get_center().get_y()), (1, 2))
    cp = c.get_center()
    test('Method set_center() does not create new Point', lambda: c.get_center(), cp)
    test('Method set_radius() is void', lambda: type(c.set_radius(8)), type(None))
    test('Method set_radius(8) updates radius', lambda: c.get_radius(), 8)
    test('Method set_radius(-1) sets radius to 0', lambda: c2.set_radius(-1) or c2.get_radius(), 0)
    test('Method get_area() returns ~201.06', lambda: round(c.get_area(), 2), 201.06)
    test('Method __str__() returns formatted string', lambda: ''.join(str(c).split()), 'Circle:Center:(1,2)Radius:8Area:'
         + str(c.get_area() if hasattr(c, 'get_area') else 201.06))

    # p = test('Point exists', lambda: point.Point())
    # test('Constructor sets (x,y) to (0,0)', lambda: tuple(p.__dict__.values()), (0, 0))
    # test('Method get_x() returns 0', lambda: p.get_x(), 0)
    # test('Method get_y() returns 0', lambda: p.get_y(), 0)
    # test('Method set_x() is void', lambda: type(p.set_x(5.5)), type(None))
    # test('Method set_x(5.5) updates x', lambda: p.get_x(), 5.5)
    # test('Method set_y() is void', lambda: type(p.set_y(10)), type(None))
    # test('Method set_y(10) updates y', lambda: p.get_y(), 10)
    # test('Method __str__() returns (5,10)', lambda: str(p), '(5.5,10)')


main()