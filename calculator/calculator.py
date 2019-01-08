"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""
    s = s.split(" ")
    operators = {"+", "-", "*", "/"}
    ops_stack = []
    num_stack = []

    for char in s:
        if char in operators:
            ops_stack.append(char)
        elif char.isdigit():
            num_stack.append(int(char))

    while ops_stack:
        op = ops_stack.pop()
        num1 = num_stack.pop()
        num2 = num_stack.pop()

        if op == "+":
            num_stack.append(num1 + num2)
        elif op == "-":
            num_stack.append(num2 - num1)
        elif op == "*":
            num_stack.append(num1 * num2)
        elif op == "/":
            num_stack.append(num2//num1) # floor division

    return num_stack.pop()


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
