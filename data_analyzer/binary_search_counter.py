def count_binSearch(content):
    method_name = "binarySearch"
    count = 0
    stack = []

    # Split the code into lines for parsing
    lines = content.splitlines()

    for line in lines:
        # Remove leading and trailing whitespace from the line
        line = line.strip()

        # Check for opening and closing brackets in the line
        opening_brackets = line.count("(")
        closing_brackets = line.count(")")

        # Update the stack based on bracket counts
        for _ in range(closing_brackets):
            if stack and stack[-1] == method_name:
                stack.pop()

        # Check if the line contains a method call
        if method_name in line and "(" in line:
            count += 1

            # Update stack based on opening bracket count
            for _ in range(opening_brackets):
                stack.append(method_name)

    return count