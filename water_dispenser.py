from collections import deque

litters = int(input())
people = deque()
while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    data = input()
    if data == "End":
        break

    if data.startswith("refill "):
        litters += int(data.split()[1])

    else:
        person = people.popleft()
        water_need = int(data)

        if water_need <= litters:
            print(f"{person} got water")
            litters -= water_need
        else:
            print(f"{person} must wait")

print(f"{litters} liters left")
