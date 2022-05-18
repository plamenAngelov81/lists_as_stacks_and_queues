from collections import deque


class Crossroad:
    def __init__(self, green_light, window):
        self.green_light = green_light
        self.window = window
        self.cars = deque()

    def process(self):

        data = input()

        passed_cars = 0
        condition = False

        while True:
            if data == "END":
                break
            if data == "green":

                if self.cars:
                    current_car = self.cars.popleft()
                    time_left = self.green_light - len(current_car)
                    while time_left > 0:
                        passed_cars += 1
                        if self.cars:
                            current_car = self.cars.popleft()
                            time_left -= len(current_car)
                        else:
                            break
                    if time_left == 0:
                        passed_cars += 1

                    if self.window >= abs(time_left):
                        if time_left < 0:
                            passed_cars += 1
                    else:
                        index = self.window + time_left
                        print("A crash happened!")
                        print(f"{current_car} was hit at {current_car[index]}.")
                        condition = True
                        break
            else:
                self.cars.append(data)

            data = input()

        if not condition:
            print("Everyone is safe.")
            print(f"{passed_cars} total cars passed the crossroads.")


obj = Crossroad(green_light=int(input()), window=int(input()))
obj.process()
