import random


def random_integer_in_range(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.

    Args:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    Returns:
        int: A random integer between min_value and max_value.
    
    """
    return random.randint(min_value, max_value)


def random_arithmetic_operator():
    """
    Randomly selects an arithmetic operator.
    
    Returns:
        str: A randomly chosen arithmetic operator: '+', '-', or '*'.

    """
    
    return random.choice(['+', '-', '*'])


def arithmetic_operation(first_operand, second_operand, arithmetic_operator):
    """
    Calculates an arithmetic operation between given first and second operand with given operator.

    Args:
        first_operand (int): First value of the calculation.
        second_operand (int): Second value of the operation.

    Returns:
        tuple: A tuple of a string containing the arithmetic operation and the result of the operation.
    
    """
    operation_str = f"{first_operand} {arithmetic_operator} {second_operand}"

    if arithmetic_operator == '+':
        result = first_operand + second_operand
    elif arithmetic_operator == '-':
        result = first_operand - second_operand
    elif arithmetic_operator == '*': 
        result = first_operand * second_operand
    else:
        raise ValueError("Unsupported operator. Please use '+', '-', or '*'.")

    return operation_str, result

def math_quiz():
    """
    Performs an interactive math quiz.

    Random arithmetic operations are printed to the console and presented to the user.
    Input result is checked against correct result.
    Correct answers are counted in the score.

    Returns:
        None
    
    """
    score = 0               # Amount of correctly answered questions
    test_questions = 3      # Total amount of test questions in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(test_questions):
        n1 = random_integer_in_range(1, 10)
        n2 = random_integer_in_range(1, 5)
        o = random_arithmetic_operator()

        PROBLEM, ANSWER = arithmetic_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        # Handle invalid input
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid answer. Please enter a number.")
            continue

        # Check input against correct result
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{test_questions}")

if __name__ == "__main__":
    math_quiz()
