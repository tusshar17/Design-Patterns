class Equipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Composite:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self

    @property
    def price(self):
        return sum([x.price for x in self.items])

    @price.setter
    def price(self, value):
        self.price = value


computer = Composite("PC")
processor = Equipment("Processor", 15000)
hdd = Equipment("HDD", 3000)
ram = Equipment("RAM", 2000)
rom = Equipment("ROM", 7000)

mem = Composite("Memory")
mem.add(ram).add(rom)

pc = computer.add(processor).add(hdd).add(mem)

print(pc.price)
