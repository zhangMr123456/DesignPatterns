"""
单例模式: 全局只能出现一个对象
"""
import threading

"""
第一种: 纯天然
    Python是编译性语言,运行时会编译为 .pyc 字节码文件,所以只需要导入使用就是纯天然的单例模式了
"""

class Singleton:
    pass

singleton = Singleton()


"""
第二种: 装饰器实现
    定义一个装饰器,然后对类进行装饰这样就可以实现单例了
"""


def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton


"""
第三种: 实用类实现
    在类中定义方法取的对象而不是通过 __init__() 这样就可以实现单例了
    缺点就是只能通过类方法来限制,如果直接调 ClassName() 用依旧会创建多个对象
    threading.Lock(): 保证线程安全,统一
"""

class Singleton:
    _instance_lock  = threading.Lock()

    def __init__(self, *args, **kwargs):
        print("初始化...")
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(Singleton, "_instance"):
                cls._instance = cls(*args, **kwargs)
        return cls._instance


"""
第四种: 使用 __new__() 特殊方法实现,以为 __new__() 是创建类示例的地方,所以在正常创建的时候可以重写进行判断
    这样不会影响正常使用,也是比较推荐的做法,可以写一个 BaseMeta 类让需要实现单例的类去继承,完成单例的实现
    这样在编写基础单例类的时候一定不能使用 cls.__new__() 这样会自己调自己锁死报错,要使用 object的 __new__()
"""

class Singleton:
    _instance_lock = threading.Lock()

    def __init__(self):
        print("初始化...")

    def __new__(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(Singleton, "_instance"):
                cls._instance = object.__new__(cls)
        return cls._instance


"""
第五种: 使用 metaclass 实现
    使用 metaclass 定义构造类然后让类指定 metaclass 这样也可以实现单例
"""

class MetaClass(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(cls, "_instance"):
                print("创建了一次")
                cls._instance = super(MetaClass, cls).__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=MetaClass):
    pass


