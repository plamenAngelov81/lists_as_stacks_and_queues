from collections import deque

customer_list = deque()

while True:
    name = input()
    if name == "End":
        print(f"{len(customer_list)} people remaining.")
        break
    elif name == "Paid":
        while customer_list:
            print(customer_list.popleft())
    else:
        customer_list.append(name)
