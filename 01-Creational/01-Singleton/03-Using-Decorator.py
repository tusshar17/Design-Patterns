def singleton(cls):
    instances = {}

    def get_instances(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instances


@singleton
class DatabaseConnection:
    def __init__(self):
        print("Creating database connection...")


db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1)
print(db2)
