class FormulaError(Exception):
    pass


def calculate(formula):
    try:
        values = formula.split()
        
        # If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception        
        if len(values) != 3:
            raise FormulaError("Invalid formula")

        # convert the first and third input to a float
        num1 = float(values[0])
        operator = values[1]
        num2 = float(values[2])

        # catch ValueError that occurs, and instead raise a FormulaError
        if operator not in ['+', '-']:
            raise FormulaError("Invalid operator")

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2

        print("Result:", result)

    except ValueError:
        # If the second input is not '+' or '-', again raise a FormulaError
        raise FormulaError("Invalid value")


while True:
    user_input = input("Enter a formula (e.g., 1 + 1), or 'quit' to exit: ")
    if user_input.lower() == 'quit' or user_input.lower() == 'q':
        break

    try:
        calculate(user_input)
    except FormulaError as e:
        print("Error:", e)
