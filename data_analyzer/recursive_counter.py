import re


def count_recursive(content):#se existir mais de uma função recursiva como faço?
    # Use a regular expression to find all function definitions in the Java code
    function_definitions = re.findall(r'\b\s*void\s+(\w+)\s*\(', content)

    # Initialize a dictionary to store the number of recursive calls for each function
    recursive_calls_count = {}

    for function_name in function_definitions:
        # Use a regular expression to find all function calls to the current function
        pattern = r'\b' + function_name + r'\s*\('
        matches = re.findall(pattern, content)

        # Store the number of recursive calls for the current function
        recursive_calls_count[function_name] = len(matches)

    return len(matches)
    


