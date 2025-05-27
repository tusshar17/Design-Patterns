from dataclasses import dataclass


class ComplexSystemStorage:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.cache = {}
        print(f"Reading data from file: {filePath}")

    def store(self, key: str, value: str):
        self.cache[key] = value

    def read(self, key: str):
        return self.cache[key]

    def commit(self):
        print(f"Storing cached data to file {self.filePath}")


@dataclass
class User:
    login: str


# Facade
class UserRepository:
    def __init__(self):
        self.system_preference = ComplexSystemStorage("/data/default.prefs")

    def save(self, user: User):
        self.system_preference.store("USER_KEY", user)
        self.system_preference.commit()

    def find_first(self):
        return User(self.system_preference.read("USER_KEY"))


user = User("user")

user_repository = UserRepository()

user_repository.save(user)
retrieved_user = user_repository.find_first()
print(retrieved_user.login)
