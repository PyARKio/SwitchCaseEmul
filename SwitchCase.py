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

    def case(self):
        return True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


if __name__ == '__main__':
    with switch('1') as s:
        ...
