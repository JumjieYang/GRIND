from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.passenger_map = {}
        self.travel_data = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger_map[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.passenger_map[id]

        self.travel_data[(start_station, stationName)][0] += t - start_time
        self.travel_data[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_count = self.travel_data[(startStation, endStation)]

        if total_count == 0:
            return 0

        return total_time / total_count
