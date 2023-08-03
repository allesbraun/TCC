import re


def count_nested_loops(content):
    # Regular expressions to match for and while loops
    for_loop_pattern = r'\bfor\s*\([^)]*\)\s*{'
    while_loop_pattern = r'\bwhile\s*\([^)]*\)\s*{'

    # Count the occurrences of nested loops
    num_nested_loops = len(re.findall(f'({for_loop_pattern}|{while_loop_pattern})', content))

    return num_nested_loops
