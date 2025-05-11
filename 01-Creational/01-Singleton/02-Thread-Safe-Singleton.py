import time
from threading import Thread, Lock


class Singleton(type):
    """A meta class for Singleton pattern"""

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                time.sleep(1)
                cls._instances[cls] = instance
        return cls._instances[cls]


class NetworkDriver(metaclass=Singleton):
    def log(self):
        print(f"{self}\n")


def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton


if __name__ == "__main__":
    # Single Thread
    # s1 = create_singleton()
    # s2 = create_singleton()

    # Multi Thread
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)
    p1.start()
    p2.start()
