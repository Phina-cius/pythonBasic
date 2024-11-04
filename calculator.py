class stringAnalyzer:
    # Method for characters
    def separate_characters(self, input_string):
        characters = []
        for char in input_string:
            if char.isalpha():
                characters.append(char)
        return characters

    # Method for numbers
    def separate_numbers(self, input_string):
        numbers = []
        for char in input_string:
            if char.isnumeric():
                numbers.append(char)
        return numbers

    # Method for symbols
    def separate_symbols(self, input_string):
        characters = []
        integers = []
        symbols = []
        for char in input_string:
            if char.isalpha():
                characters.append(char)
            elif char.isdigit():
                integers.append(char)
            else:
                symbols.append(char)
        return characters, integers, symbols


class Calculator:
    def __init__(self):
        self.analyzer = stringAnalyzer()

    def evaluate_expression(self, input_string):
        # Directly use the input string as the expression
        expression = input_string

        # Debugging print statement
        print(f"Expression: {expression}")

        try:
            # Evaluate the expression
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error evaluating expression: {e}"





#the loop
option='y'

while option=='y':
    # Example usage
    calculator = Calculator()
    input_string = input("please enter the expression")
    result = calculator.evaluate_expression(input_string)
    print(f"Result: {result}")

    option = input("please type choose 'y' or 'n'")


print("bye")

