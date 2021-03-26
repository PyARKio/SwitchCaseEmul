# -- coding: utf-8 --
from __future__ import unicode_literals


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class switch:
    def __init__(self, value):
        self.value = value

    def default(self):
        return True

    def case(self, val):
        if val == self.value:
            return True
        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


if __name__ == '__main__':
    with switch('1') as s:
        print(s.case(1))
        print(s.case(2))
        print(s.case(3))
        print(s.case('1'))
        print(s.case(3))
