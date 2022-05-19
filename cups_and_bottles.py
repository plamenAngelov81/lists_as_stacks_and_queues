from collections import deque


class CupBottle:
    def __init__(self, cups, bottles):
        self.cups = cups
        self.bottles = bottles

    def process(self):
        queue_cups = deque(self.cups)
        waste_water = 0
        while queue_cups and self.bottles:
            current_cup = queue_cups[0]
            current_bottle = self.bottles[-1]

            if current_bottle >= current_cup:
                water_left = current_bottle - current_cup
                waste_water += water_left
                queue_cups.popleft()
                self.bottles.pop()

            elif current_bottle < current_cup:
                queue_cups[0] -= current_bottle
                self.bottles.pop()

        if queue_cups:
            cub_result = ' '.join([str(x) for x in queue_cups])
            print(f"Cups: {cub_result}")
        if self.bottles:
            bottle_result = ' '.join([str(x) for x in self.bottles])
            print(f"Bottles: {bottle_result}")

        print(f"Wasted litters of water: {waste_water}")


obj = CupBottle(cups=list(map(int, input().split())), bottles=list(map(int, input().split())))
obj.process()
