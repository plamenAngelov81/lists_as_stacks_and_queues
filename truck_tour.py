from collections import deque


class TruckTour:
    def __init__(self, petrol_pumps):
        self.petrol_pumps = petrol_pumps
        self.pump_queue = deque()

    def circle(self):
        for i in range(self.petrol_pumps):
            pump_data = list(map(int, input().split()))
            self.pump_queue.append(pump_data)

    def process(self):
        counter = 0
        while True:
            fuel_left = 0
            for fuel, distance in self.pump_queue:
                concurrent_fuel = fuel + fuel_left
                if concurrent_fuel < distance:
                    counter += 1
                    self.pump_queue.append(self.pump_queue.popleft())
                    break
                else:
                    fuel_left = concurrent_fuel - distance
            else:
                break

        print(counter)


obj = TruckTour(petrol_pumps=int(input()))
obj.circle()
obj.process()
