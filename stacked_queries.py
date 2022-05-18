n = int(input())
numbers = []
for i in range(1, n + 1):
    data = [int(x) for x in input().split()]
    command = data[0]
    if command == 1:
        numbers.append(int(data[1]))

    elif command == 2 and numbers:
        numbers.pop()

    elif command == 3 and numbers:
        print(max(numbers))

    elif command == 4 and numbers:
        print(min(numbers))

reversed_numbers = []
while numbers:
    num = numbers.pop()
    reversed_numbers.append(str(num))

print(", ".join(reversed_numbers))



