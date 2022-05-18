from collections import deque

food_quantity = int(input())

daily_orders = (list(map(int, input().split())))

print(max(daily_orders))
daily_orders_queue = deque(daily_orders)
start_index = 0

for j in range(len(daily_orders)):
    if food_quantity >= daily_orders[j]:
        food_quantity -= daily_orders[j]
        daily_orders_queue.popleft()
    else:
        start_index = j
        break

if len(daily_orders_queue) == 0:
    print("Orders complete")
else:
    orders_left = list(map(str, daily_orders[start_index:]))

    print(f"Orders left: {' '.join(orders_left)}")
