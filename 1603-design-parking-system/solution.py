class ParkingSystem:

    def __init__(self, big, medium, small):
        self.list = [0, big, medium, small]

    def addCar(self, carType):
        if self.list[carType] == 0:
            return False

        self.list[carType] -= 1

        return True
