import point
from tester import test


def main():
    test('Point exists', lambda: point.Point)
    p = test('Constructor takes no args', lambda: point.Point())
    test('Constructor sets (x,y) to (0,0)', lambda: tuple(p.__dict__.values()), (0, 0))
    test('Method get_x() returns 0', lambda: p.get_x(), 0)
    test('Method get_y() returns 0', lambda: p.get_y(), 0)
    test('Method set_x() is void', lambda: type(p.set_x(5.5)), type(None))
    test('Method set_x(5.5) updates x', lambda: p.get_x(), 5.5)
    test('Method set_y() is void', lambda: type(p.set_y(10)), type(None))
    test('Method set_y(10) updates y', lambda: p.get_y(), 10)
    test('Method __str__() returns (5.5,10)', lambda: str(p).replace(' ', ''), '(5.5,10)')


main()