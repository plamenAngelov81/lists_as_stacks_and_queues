class BalancedParentheses:
    def __init__(self, parentheses):
        self.parentheses = parentheses
        self.balance_dict = {
            "(": ")", 
            "{": "}", 
            "[": "]"
        }
        self.brackets = []

    def process(self):
        condition = True
        for bracket in self.parentheses:
            if bracket in "({[":
                self.brackets.append(bracket)
            elif not self.brackets:
                condition = False
                break
            else:
                last_open_bracket = self.brackets.pop()
                if self.balance_dict[last_open_bracket] != bracket:
                    condition = False
                    break

        if condition and len(self.brackets) == 0:
            print("YES")
        else:
            print("NO")


obj = BalancedParentheses(parentheses=input())
obj.process()
