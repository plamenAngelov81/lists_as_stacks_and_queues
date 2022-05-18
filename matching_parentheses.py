some_string = input()

bracket_list = []

for i in range(len(some_string)):
    if some_string[i] == "(":
        bracket_list.append(i)
    elif some_string[i] == ")":
        start = bracket_list.pop()
        end = i
        print(some_string[start:end + 1])
