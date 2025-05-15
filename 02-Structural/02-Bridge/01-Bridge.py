from abc import ABC, abstractmethod


class Device(ABC):
    volume = 0

    @abstractmethod
    def get_name(self) -> str:
        pass


class Radio(Device):
    def get_name(self):
        return f"Radio {self}"


class TV(Device):
    def get_name(self):
        return f"TV {self}"


class Remote(ABC):
    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass


class BasicRemote(Remote):
    def __init__(self, device: Device):
        self.device = device

    def volume_up(self):
        self.device.volume += 1
        print(f"{self.device.get_name()} Volume up: {self.device.volume}")

    def volume_down(self):
        if self.device.volume > 0:
            self.device.volume -= 1
        print(f"{self.device.get_name()} Volume down: {self.device.volume}")


radio = Radio()
tv = TV()

radio_remote = BasicRemote(radio)
tv_remote = BasicRemote(tv)

tv_remote.volume_up()
tv_remote.volume_up()
tv_remote.volume_down()

radio_remote.volume_up()
radio_remote.volume_down()
radio_remote.volume_down()
