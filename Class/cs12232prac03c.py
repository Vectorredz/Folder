from dataclasses import dataclass

@dataclass(frozen = True)
class Point:
    x: int
    y: int
    z: int

class Movements(Point):
    def __init__(self,point: Point):
        self.point = point
        self.visited_points: set[Point] = set()
        self.visited_points.add(self.point)

    def move_to(self, dir: str) -> None:
        delta: dict[str, tuple[int,int,int]] = {'+x': (1,0,0),
                '-x':(-1,0,0),
                '+y':(0,1,0),
                '-y': (0,-1,0),
                '+z':(0,0,+1),
                '-z':(0,0,-1)
        }
        if dir in delta:
            dx, dy, dz = delta[dir]
            new_point = Point(self.point.x + dx, self.point.y + dy, self.point.z + dz)
        
        self.visited_points.add(new_point)
    def teleport_to(self, point: Point) -> None:
        self.point = point
        self.visited_points.add(self.point)
    def visited(self) -> set[Point]:
        return self.visited_points
    def visited_count(self) -> int:
        return len(self.visited_points)
    

m = Movements(Point(10, -30, 0))
m.move_to("+x")
m.teleport_to(Point(0,0,0))
print(m.visited())