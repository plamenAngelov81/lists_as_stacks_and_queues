from collections import deque


class Revolver:
    def __init__(self, price_per_ammo, magazine_size, ammo_size, locks, reward):
        self.price_per_ammo = price_per_ammo
        self.magazine_size = magazine_size
        self.ammo_size = ammo_size
        self.locks = locks
        self.reward = reward

    def process(self):
        queue_locks = deque(self.locks)
        used_bullets = 0
        ammo_cost = 0

        while True:
            if len(self.ammo_size) == 0:
                print(f"Couldn't get through. Locks left: {len(queue_locks)}")
                break

            current_lock = queue_locks[0]
            current_bullet = self.ammo_size[-1]

            if current_bullet <= current_lock:
                print("Bang!")
                used_bullets += 1
                self.ammo_size.pop()
                if len(self.ammo_size) > 0 and used_bullets == self.magazine_size:
                    print("Reloading!")
                    used_bullets = 0
                queue_locks.popleft()
                ammo_cost += self.price_per_ammo

            elif current_bullet > current_lock:
                print("Ping!")
                used_bullets += 1
                self.ammo_size.pop()
                if len(self.ammo_size) > 0 and used_bullets == self.magazine_size:
                    print("Reloading!")
                    used_bullets = 0
                ammo_cost += self.price_per_ammo

            if len(queue_locks) == 0:
                bullets_left = len(self.ammo_size)
                salary = self.reward - ammo_cost
                print(f"{bullets_left} bullets left. Earned ${salary}")
                break


obj = Revolver(price_per_ammo=int(input()), magazine_size=int(input()), ammo_size=list(map(int, input().split())),
               locks=list(map(int, input().split())), reward=int(input()))
obj.process()
