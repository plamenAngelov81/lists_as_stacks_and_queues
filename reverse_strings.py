class Rev:
    def __init__(self, some_string):
        self.some_string = some_string
        rev_string = some_string[::-1]
        print(rev_string)


obj = Rev(some_string=input())


