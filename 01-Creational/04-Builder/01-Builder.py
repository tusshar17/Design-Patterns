class Computer:
    def __init__(self, cpu=None, ram=None, storage=None, gpu=None, os=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.os = os

    def __str__(self):
        return (
            f"Computer Specs:\n"
            f"CPU: {self.cpu}\nRAM: {self.ram}\n"
            f"Storage: {self.storage}\nGPU: {self.gpu}\nOS: {self.os}"
        )


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_os(self, os):
        self.computer.os = os
        return self

    def build(self):
        return self.computer


# usage
builder = ComputerBuilder()
gaming_pc = (
    builder.set_cpu("Intel i9")
    .set_gpu("NVIDIA RTX 4090")
    .set_ram("32GB")
    .set_storage("1TB SSD")
    .set_os("Windows 11")
    .build()
)

print(gaming_pc)
