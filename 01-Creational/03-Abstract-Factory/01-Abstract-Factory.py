from abc import ABC, abstractmethod


class FoodType:
    french = 1
    american = 1


class Restaurant(ABC):
    @abstractmethod
    def make_food(self):
        pass

    @abstractmethod
    def make_drink(self):
        pass


class FrenchRestaurant(Restaurant):
    def make_food(self):
        print("French food")

    def make_drink(self):
        print("French drink")


class AmericanRestaurant(Restaurant):
    def make_food(self):
        print("American food")

    def make_drink(self):
        print("American drink")


class RestaurantFactory:
    @staticmethod
    def suggest_restaurant(f_type: FoodType):
        if f_type == FoodType.american:
            return AmericanRestaurant()
        else:
            return FrenchRestaurant()


def dine_at(restaurant: Restaurant):
    print("For dinner we are having:")
    restaurant.make_food()
    restaurant.make_drink()


# example usage
suggestion1 = RestaurantFactory.suggest_restaurant(FoodType.french)
suggestion2 = RestaurantFactory.suggest_restaurant(FoodType.american)

dine_at(suggestion1)
dine_at(suggestion2)
