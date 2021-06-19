"""
抽象工厂模式: 抽象工厂模式就是将工厂作为子类进一步建造一个更大的工厂来制造工厂,通过制造的工厂进行生产
"""

from factory_pattern import FoodFactory, AnimalFactory


class AbstractFactory:
    """抽闲工厂"""

    def get_factory(self, f):
        if f == "Food":
            return FoodFactory()
        elif f == "Animal":
            return AnimalFactory()


if __name__ == '__main__':
    abstract_factory = AbstractFactory()
