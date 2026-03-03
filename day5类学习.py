# shape定义
from abc import ABC, abstractmethod # 要先import 抽象基类

class Shape(ABC):
    _count = 0 # 受保护，记录图形被搭建的个数
    def __init__(self):
        Shape._count += 1 # 被调用就+1
        self.__area = None

    @abstractmethod
    def _calc_area(self):
        # 子类重新定义计算面积的方法
        pass

    def get_area(self):
        # 封装受保护方法，获得area的
        if self.__area is None:
            self.__area = self._calc_area()
        return self.__area

    @classmethod
    def get_count(cls):
        # 调用类变量，获得搭建次数
        return cls._count

class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        self.__height = height # 保护变量
        self.__width = width

    def _calc_area(self):
        return self.__height * self.__width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius # 保护变量

    def _calc_area(self):
        return self.__radius **2 * 3.14159

if __name__ == '__main__':
    d = Circle(4)
    e = Rectangle(5, 6)
    print(e.get_area())
    print(d.get_area())
    print(e.get_count())

# str.strip()
import string
s = "\f\n\t Hello \nWorld  \n\r"
print(s.strip())
# 删字符串组左右两边的python定义的空白，不能精确消除空格键