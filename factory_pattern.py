"""
工厂设计模式
"""

class Animal:
    """公公抽象父类定义方法,让子类去实现
    """
    def eat(self):
        raise AttributeError


class Cat(Animal):
    """子类实现了父类的方法
    """
    def eat(self):
        print("猫在吃东西")


class Dog(Animal):
    """子类实现了父类的方法
    """
    def eat(self):
        print("狗在吃东西")


class AnimalFactory:
    """动物工厂: 工厂类只需要传入相应字符串就可以生成对应的类型
    """
    def get_eat(self, t):
        if t == "Cat":
            return Cat()
        elif t == "Dog":
            return Dog()
        return None


class Food:
    def by_eat(self):
        raise AttributeError("此方法必须实现")


class Banana(Food):
    def by_eat(self):
        print("香蕉被吃")


class Bread(Food):
    def by_eat(self):
        print("面包被吃")


class FoodFactory:
    """食物工厂: 工厂类只需要传入相应字符串就可以生成对应的类型
    """
    def get_eat(self, f):
        if f == "Banana":
            return Banana()
        elif f == "Bread":
            return Bread()
        return None


if __name__ == '__main__':
    factory = AnimalFactory()
    animal = factory.get_eat("Dog")
    animal.eat()