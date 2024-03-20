from dataclasses import dataclass, InitVar
 
@dataclass
class City:
    name: str
    psgc: str
    population: int
    households: int
    barangays: int
    area: float
    area_in: InitVar[bool] = False
    def __post_init__(self, area_in: bool):
        if area_in:
            self.area *= 2.59
    def squarePerMeter(self) -> float:
        return city.population / city.area

city = City(
    name='Quezon City',
    psgc='137404000',
    population=2_960_048,
    households=738_724,
    barangays=142,
    area=171.71, 
)                 
      
print(city.area)