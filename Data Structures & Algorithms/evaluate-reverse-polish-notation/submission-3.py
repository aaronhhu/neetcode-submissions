class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        output = 0
        first = 0
        second = 0



        for i in range(len(tokens)):
            if tokens[i] in operators:
                second = stack.pop()
                first = stack.pop()
                match tokens[i]:
                    case "+":
                        output = first + second
                    case "-":
                        output = first - second
                    case "*":
                        output = first * second
                    case "/":
                        output = first / second
                stack.append(int(output))
            else:
                stack.append(int(tokens[i]))

        return stack.pop()