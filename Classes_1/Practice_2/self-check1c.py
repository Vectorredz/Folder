class WaterStation:
    def __init__(self):
        self.stations: dict[int, int] = {}

    def add_water_station(self, position: int) -> None:
        if position not in self.stations:
            self.stations[position] = 1
        elif position in self.stations:
            self.stations[position] += 1

    def count_water_stations(self, a: int, b: int) -> int:
        counter: int = 0
        if a > b:
            return None
        else:
            for i in range(a, b+1):
                if i in self.stations:
                    counter += self.stations[i]
        return counter
    def __repr__(self):
        return f"{self.stations}"
w = WaterStation()
assert w.count_water_stations(-100, 100) == 0
assert w.count_water_stations(12, 12) == 0
assert w.count_water_stations(0, 12) == 0
assert w.count_water_stations(0, 11) == 0
assert w.count_water_stations(0, 1) == 0

w.add_water_station(12)
assert w.count_water_stations(-100, 100) == 1
assert w.count_water_stations(12, 12) == 1
assert w.count_water_stations(0, 12) == 1
assert w.count_water_stations(0, 11) == 0
assert w.count_water_stations(0, 1) == 0

w.add_water_station(10)
assert w.count_water_stations(-100, 100) == 2
assert w.count_water_stations(12, 12) == 1
assert w.count_water_stations(0, 12) == 2
assert w.count_water_stations(0, 11) == 1
assert w.count_water_stations(0, 1) == 0

w.add_water_station(12)
assert w.count_water_stations(-100, 100) == 3
assert w.count_water_stations(12, 12) == 2
assert w.count_water_stations(0, 12) == 3
assert w.count_water_stations(0, 11) == 1
assert w.count_water_stations(0, 1) == 0

print(w)